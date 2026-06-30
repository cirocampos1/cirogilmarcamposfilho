import json
import re
from pathlib import Path

SKILLS_DIR = Path("/home/leonardobarbosa/dev/autoresearch/.agent/skills")
MANIFEST_PATH = SKILLS_DIR / "skills_index.json"

def get_skill_metadata(skill_path: Path):
    content = skill_path.read_text()

    # Extract name and description from frontmatter
    name = skill_path.parent.name
    description = ""

    frontmatter_match = re.search(r"^---\n(.*?)\n---", content, re.DOTALL)
    if frontmatter_match:
        fm_content = frontmatter_match.group(1)
        for line in fm_content.split("\n"):
            if line.startswith("name:"):
                name = line.split(":", 1)[1].strip()
            elif line.startswith("description:"):
                description = line.split(":", 1)[1].strip()

    return {
        "id": skill_path.parent.name,
        "path": str(skill_path.parent.relative_to(SKILLS_DIR.parent)), # Path relative to .agent
        "name": name,
        "description": description,
        "version": "3.0",
        "architecture_focus": "Option B"
    }

def generate_manifest():
    print(f"Generating manifest from {SKILLS_DIR}...")
    skills = []
    # Find all SKILL.md files
    for skill_path in SKILLS_DIR.rglob("SKILL.md"):
        # Avoid templates if they are not intended to be picked up directly
        if "templates" in str(skill_path):
            continue
        try:
            metadata = get_skill_metadata(skill_path)
            skills.append(metadata)
        except Exception as e:
            print(f"Error processing {skill_path}: {e}")

    # Sort by ID for consistency
    skills.sort(key=lambda x: x["id"])

    with open(MANIFEST_PATH, 'w') as f:
        json.dump(skills, f, indent=2)

    print(f"Manifest generated with {len(skills)} entries at {MANIFEST_PATH}")

if __name__ == "__main__":
    generate_manifest()
