import re
from pathlib import Path

SKILLS_DIR = Path("/home/leonardobarbosa/dev/autoresearch/.agent/skills")

def verify_skill(skill_path: Path):
    if not skill_path.exists():
        return False, "File not found"

    content = skill_path.read_text()

    errors = []

    # Check Frontmatter
    frontmatter_match = re.search(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not frontmatter_match:
        return False, "Missing frontmatter"

    fm_content = frontmatter_match.group(1)

    # Required V3 fields
    if "version: 3.0" not in fm_content:
        errors.append("Version 3.0 missing")
    if 'architecture_focus: "Option B"' not in fm_content:
        errors.append('Architecture Focus "Option B" missing')
    if "last_updated:" not in fm_content:
        errors.append("Last Updated missing")
    if "verification_script:" not in fm_content:
        errors.append("Verification Script missing")

    # Check Option B Guidelines
    if "Option B: Efficiency Guidelines" not in content:
        errors.append("Missing Option B Rules")

    if errors:
        return False, ", ".join(errors)
    return True, "OK"

def main():
    print(f"Auditing Skills in {SKILLS_DIR}...")
    total = 0
    passed = 0
    failed_list = []

    # Walk recursively to find all SKILL.md files
    for skill_path in SKILLS_DIR.rglob("SKILL.md"):
        total += 1
        is_ok, msg = verify_skill(skill_path)
        if is_ok:
            passed += 1
        else:
            failed_list.append(f"{skill_path.relative_to(SKILLS_DIR)}: {msg}")

    print(f"\nAudit complete: {passed}/{total} passed.")
    if failed_list:
        print("\nFailed Skills:")
        for f in failed_list:
            print(f"❌ {f}")
    else:
        print("✅ All skills compliant!")

if __name__ == "__main__":
    main()
