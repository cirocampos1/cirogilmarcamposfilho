import re
from datetime import datetime
from pathlib import Path

SKILLS_DIR = Path("/home/leonardobarbosa/dev/autoresearch/.agent/skills")
EXPERIMENTS_FILE = SKILLS_DIR / "experiments.json"
DATE_STR = datetime.now().strftime("%Y-%m-%d")

V3_RULES = """
## 🚀 Option B: Efficiency Guidelines (MANDATORY)

1. **Direct Action**: Never explain what you are going to do. Just do it.
2. **Token Economy**: Minimize chatter. Use the most concise tool calls possible.
3. **Verification First**: Run validation scripts immediately after any change.
4. **GPU Acceleration**: Use local GPU/Ollama for heavy analysis tasks when possible.
"""

def upgrade_skill(skill_path: Path):
    if not skill_path.exists():
        return False

    content = skill_path.read_text()

    # Update Frontmatter
    frontmatter_match = re.search(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not frontmatter_match:
        print(f"Skipping {skill_path}: No frontmatter found.")
        return False

    fm_content = frontmatter_match.group(1)
    fm_lines = fm_content.split("\n")
    fm_dict = {}
    for line in fm_lines:
        if ":" in line:
            k, v = line.split(":", 1)
            fm_dict[k.strip()] = v.strip()

    # Set V3 standardization
    fm_dict["version"] = "3.0"
    fm_dict["architecture_focus"] = '"Option B"'
    fm_dict["last_updated"] = DATE_STR
    if "verification_script" not in fm_dict:
        fm_dict["verification_script"] = '"scripts/verify.py"'

    new_fm = "---\n" + "\n".join([f"{k}: {v}" for k, v in fm_dict.items()]) + "\n---"
    content = content.replace(frontmatter_match.group(0), new_fm)

    # Inject Option B Rules if not present
    if "Option B: Efficiency Guidelines" not in content:
        # Try to find a good place (after frontmatter or before Related Skills)
        if "## Related Skills" in content:
            content = content.replace("## Related Skills", V3_RULES + "\n## Related Skills")
        elif "## Content Map" in content:
            content = content.replace("## Content Map", V3_RULES + "\n## Content Map")
        else:
            content += "\n" + V3_RULES

    skill_path.write_text(content)
    return True

def main():
    print(f"Starting Meta-Optimization: V3.0 Upgrade in {SKILLS_DIR}")
    count = 0
    # Walk recursively to find all SKILL.md files
    for skill_path in SKILLS_DIR.rglob("SKILL.md"):
        if upgrade_skill(skill_path):
            print(f"✅ Upgraded {skill_path.relative_to(SKILLS_DIR)}")
            count += 1

    print(f"Finished. Upgraded {count} skills.")

if __name__ == "__main__":
    main()
