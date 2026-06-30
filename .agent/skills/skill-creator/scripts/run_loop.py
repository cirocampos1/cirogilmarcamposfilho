"""Orchestrator for the skill description optimization loop.

Iteratively runs evaluations and calls for improvements until a score threshold
is met or max iterations are reached.
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

from scripts.utils import parse_skill_md


def run_loop(
    eval_set_path: Path,
    skill_path: Path,
    model: str,
    max_iterations: int = 5,
    target_score: float = 1.0,
    verbose: bool = False,
) -> None:
    """Run the optimization loop."""
    timestamp = datetime.now().strftime("%Y%m%dT%H%M%S")
    work_dir = Path("work") / f"loop_{timestamp}"
    work_dir.mkdir(parents=True, exist_ok=True)

    name, current_description, _ = parse_skill_md(skill_path)
    history: list[dict] = []
    best_score = -1.0
    best_description = current_description

    for i in range(max_iterations):
        print(f"\n--- Iteration {i+1}/{max_iterations} ---")
        print(f"Testing description: \"{current_description}\"")

        # 1. Run Eval
        eval_output_path = work_dir / f"eval_iter_{i}.json"
        eval_cmd = [
            sys.executable, "-m", "scripts.run_eval",
            "--eval-set", str(eval_set_path),
            "--skill-path", str(skill_path),
            "--description", current_description,
            "--model", model,
        ]
        if verbose:
            print(f"Running: {' '.join(eval_cmd)}")
        
        result = subprocess.run(eval_cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error running eval: {result.stderr}", file=sys.stderr)
            break
        
        eval_results = json.loads(result.stdout)
        eval_output_path.write_text(result.stdout)
        
        score = eval_results["summary"]["passed"] / eval_results["summary"]["total"]
        print(f"Score: {eval_results['summary']['passed']}/{eval_results['summary']['total']} ({score*100:.1f}%)")

        if score > best_score:
            best_score = score
            best_description = current_description

        if score >= target_score:
            print("Target score reached!")
            break

        if i == max_iterations - 1:
            print("Max iterations reached.")
            break

        # 2. Improve Description
        print("Requesting improvement...")
        history_path = work_dir / f"history_iter_{i}.json"
        history_path.write_text(json.dumps(history, indent=2))
        
        improve_cmd = [
            sys.executable, "-m", "scripts.improve_description",
            "--eval-results", str(eval_output_path),
            "--skill-path", str(skill_path),
            "--model", model,
        ]
        if history:
            improve_cmd.extend(["--history", str(history_path)])
            
        result = subprocess.run(improve_cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error improving description: {result.stderr}", file=sys.stderr)
            break
            
        improve_output = json.loads(result.stdout)
        current_description = improve_output["description"]
        history = improve_output["history"]

    print(f"\nLoop complete. Best score: {best_score*100:.1f}%")
    print(f"Best description: \"{best_description}\"")

    # Update SKILL.md with best description if user wants? 
    # For now, just print it or save to a file.
    (work_dir / "best_description.txt").write_text(best_description)
    
    # Optionally update the actual SKILL.md
    update_skill_md(skill_path, best_description)
    print(f"Updated {skill_path}/SKILL.md with the best description.")


def update_skill_md(skill_path: Path, new_description: str) -> None:
    """Update the description in SKILL.md."""
    skill_md = skill_path / "SKILL.md"
    content = skill_md.read_text()
    
    # Simple regex replacement for description in frontmatter
    # This assumes description is a single line or well-formatted
    new_content = re.sub(
        r'(description:\s*)"?.*?"?(\s*\n)',
        f'\\1"{new_description}"\\2',
        content,
        flags=re.DOTALL
    )
    
    # If the above fails or is complex, we might need a better YAML parser
    # but for a script, this is a reasonable start.
    skill_md.write_text(new_content)


import re

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run optimization loop")
    parser.add_argument("--eval-set", required=True, help="Path to eval set JSON")
    parser.add_argument("--skill-path", required=True, help="Path to skill directory")
    parser.add_argument("--model", required=True, help="Model for optimization")
    parser.add_argument("--max-iterations", type=int, default=5)
    parser.add_argument("--target-score", type=float, default=1.0)
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    run_loop(
        eval_set_path=Path(args.eval_set),
        skill_path=Path(args.skill_path),
        model=args.model,
        max_iterations=args.max_iterations,
        target_score=args.target_score,
        verbose=args.verbose,
    )
