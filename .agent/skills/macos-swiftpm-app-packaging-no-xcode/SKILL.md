---
name: macos-swiftpm-app-packaging-no-xcode
description: - When the user needs a SwiftPM-based macOS app without relying on an Xcode project. - When you need packaging, signing, notarization, or appcast guidance for a SwiftPM app.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# macOS SwiftPM App Packaging (No Xcode)

## Backstory

Você é um agente especializado em macOS SwiftPM App Packaging (No Xcode).

## Contexto Original da Skill
macOS SwiftPM App Packaging (No Xcode)

## Instruções
---
name: macos-spm-app-packaging
description: Scaffold, build, sign, and package SwiftPM macOS apps without Xcode projects.
risk: safe
source: "Dimillian/Skills (MIT)"
date_added: "2026-03-25"
---

# macOS SwiftPM App Packaging (No Xcode)

## Overview
Bootstrap a complete SwiftPM macOS app folder, then build, package, and run it without Xcode. Use `assets/templates/bootstrap/` for the starter layout and `references/packaging.md` + `references/release.md` for packaging and release details.

## When to Use

- When the user needs a SwiftPM-based macOS app without relying on an Xcode project.
- When you need packaging, signing, notarization, or appcast guidance for a SwiftPM app.

## Two-Step Workflow
1) Bootstrap the project folder
   - Copy `assets/templates/bootstrap/` into a new repo.
   - Rename `MyApp` in `Package.swift`, `Sources/MyApp/`, and `version.env`.
   - Customize `APP_NAME`, `BUNDLE_ID`, and versions.

2) Build, package, and run the bootstrapped app
   - Copy scripts from `assets/templates/` into your repo (for example, `Scripts/`).
   - Build/tests: `swift build` and `swift test`.
   - Package: `Scripts/package_app.sh`.
   - Run: `Scripts/compile_and_run.sh` (preferred) or `Scripts/launch.sh`.
   - Release (optional): `Scripts/sign-and-notarize.sh` and `Scripts/make_appcast.sh`.
   - Tag + GitHub release (optional): create a git tag, upload the zip/appcast to the GitHub release, and publish.

## Minimum End-to-End Example
Shortest path from bootstrap to a running app:
```bash
# 1. Copy and rename the skeleton
cp -R assets/templates/bootstrap/ ~/Projects/MyApp
cd ~/Projects/MyApp
sed -i '' 's/MyApp/HelloApp/g' Package.swift version.env

# 2. Copy scripts
cp assets/templates/package_app.sh Scripts/
cp assets/templates/compile_and_run.sh Scripts/
chmod +x Scripts/*.sh

# 3. Build and launch
swift build
Scripts/compile_and_run.sh
```

## Validation Checkpoints
Run these after key steps to catch failures early before proceeding to the next stage.

**After packaging (`Scripts/package_app.sh`):**
```bash
# Confirm .app bundle structure is intact
ls -R build/HelloApp.app/Contents

# Check that the binary is present and executable
file build/HelloApp.app/Contents/MacOS/HelloApp
```

**After signing (`Scripts/sign-and-notarize.sh` or ad-hoc dev signing):**
```bash
# Inspect signature and entitlements
codesign -dv --verbose=4 build/HelloApp.app

# Verify the bundle passes Gatekeeper checks locally
spctl --assess --type execute --verbose build/HelloApp.app
```

**After notarization and stapling:**
```bash
# Confirm the staple ticket is attached
stapler validate build/HelloApp.app

# Re-run Gatekeeper to confirm notarization is recognised
spctl --assess --type execute --verbose build/HelloApp.app
```

## Common Notarization Failures
| Symptom | Likely Cause | Recovery |
|---|---|---|
| `The software asset has already been uploaded` | Duplicate submission for same version | Bump `BUILD_NUMBER` in `version.env` and repackage. |
| `Package Invalid:

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

- When the user needs a SwiftPM-based macOS app without relying on an Xcode project. - When you need packaging, signing, notarization, or appcast guidance for a SwiftPM app.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em macOS SwiftPM App Packaging (No Xcode)
- Para tarefas relacionadas a macos swiftpm app packaging no xcode

## Diretrizes Específicas

