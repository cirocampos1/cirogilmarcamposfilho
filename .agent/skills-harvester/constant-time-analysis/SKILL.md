---
name: constant-time-analysis
description: Analyze cryptographic code to detect operations that leak secret data through execution timing variations.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Constant-Time Analysis

## Backstory

Você é um agente especializado em Constant-Time Analysis.

## Contexto Original da Skill
Constant-Time Analysis

## Instruções
---
name: constant-time-analysis
description: "Analyze cryptographic code to detect operations that leak secret data through execution timing variations."
risk: unknown
source: community
---

# Constant-Time Analysis

Analyze cryptographic code to detect operations that leak secret data through execution timing variations.

## When to Use
```text
User writing crypto code? ──yes──> Use this skill
         │
         no
         │
         v
User asking about timing attacks? ──yes──> Use this skill
         │
         no
         │
         v
Code handles secret keys/tokens? ──yes──> Use this skill
         │
         no
         │
         v
Skip this skill
```

**Concrete triggers:**

- User implements signature, encryption, or key derivation
- Code contains `/` or `%` operators on secret-derived values
- User mentions "constant-time", "timing attack", "side-channel", "KyberSlash"
- Reviewing functions named `sign`, `verify`, `encrypt`, `decrypt`, `derive_key`

## When NOT to Use

- Non-cryptographic code (business logic, UI, etc.)
- Public data processing where timing leaks don't matter
- Code that doesn't handle secrets, keys, or authentication tokens
- High-level API usage where timing is handled by the library

## Language Selection

Based on the file extension or language context, refer to the appropriate guide:

| Language   | File Extensions                   | Guide                                                    |
| ---------- | --------------------------------- | -------------------------------------------------------- |
| C, C++     | `.c`, `.h`, `.cpp`, `.cc`, `.hpp` | references/compiled.md         |
| Go         | `.go`                             | references/compiled.md         |
| Rust       | `.rs`                             | references/compiled.md         |
| Swift      | `.swift`                          | references/swift.md               |
| Java       | `.java`                           | references/vm-compiled.md   |
| Kotlin     | `.kt`, `.kts`                     | references/kotlin.md             |
| C#         | `.cs`                             | references/vm-compiled.md   |
| PHP        | `.php`                            | references/php.md                   |
| JavaScript | `.js`, `.mjs`, `.cjs`             | references/javascript.md     |
| TypeScript | `.ts`, `.tsx`                     | references/javascript.md     |
| Python     | `.py`                             | references/python.md             |
| Ruby       | `.rb`                             | references/ruby.md                 |

## Quick Start

```bash
# Analyze any supported file type
uv run {baseDir}/ct_analyzer/analyzer.py <source_file>

# Include conditional branch warnings
uv run {baseDir}/ct_analyzer/analyzer.py --warnings <source_file>

# Filter to specific functions
uv run {baseDir}/ct_analyzer/analyzer.py --func 'sign|verify' <source_file>

# JSON output for CI
uv run {baseDir}/ct_analyzer/analyzer.py --json <source_file>
```

### Native

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Analyze cryptographic code to detect operations that leak secret data through execution timing variations.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Constant-Time Analysis
- Para tarefas relacionadas a constant time analysis

## Diretrizes Específicas

