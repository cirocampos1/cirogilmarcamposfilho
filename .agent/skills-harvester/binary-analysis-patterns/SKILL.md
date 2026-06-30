---
name: binary-analysis-patterns
description: Comprehensive patterns and techniques for analyzing compiled binaries, understanding assembly code, and reconstructing program logic.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Binary Analysis Patterns

## Backstory

Você é um agente especializado em Binary Analysis Patterns.

## Contexto Original da Skill
Binary Analysis Patterns

## Instruções
---
name: binary-analysis-patterns
description: "Comprehensive patterns and techniques for analyzing compiled binaries, understanding assembly code, and reconstructing program logic."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Binary Analysis Patterns

Comprehensive patterns and techniques for analyzing compiled binaries, understanding assembly code, and reconstructing program logic.

## Use this skill when

- Working on binary analysis patterns tasks or workflows
- Needing guidance, best practices, or checklists for binary analysis patterns

## Do not use this skill when

- The task is unrelated to binary analysis patterns
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Disassembly Fundamentals

### x86-64 Instruction Patterns

#### Function Prologue/Epilogue
```asm
; Standard prologue
push rbp           ; Save base pointer
mov rbp, rsp       ; Set up stack frame
sub rsp, 0x20      ; Allocate local variables

; Leaf function (no calls)
; May skip frame pointer setup
sub rsp, 0x18      ; Just allocate locals

; Standard epilogue
mov rsp, rbp       ; Restore stack pointer
pop rbp            ; Restore base pointer
ret

; Leave instruction (equivalent)
leave              ; mov rsp, rbp; pop rbp
ret
```

#### Calling Conventions

**System V AMD64 (Linux, macOS)**
```asm
; Arguments: RDI, RSI, RDX, RCX, R8, R9, then stack
; Return: RAX (and RDX for 128-bit)
; Caller-saved: RAX, RCX, RDX, RSI, RDI, R8-R11
; Callee-saved: RBX, RBP, R12-R15

; Example: func(a, b, c, d, e, f, g)
mov rdi, [a]       ; 1st arg
mov rsi, [b]       ; 2nd arg
mov rdx, [c]       ; 3rd arg
mov rcx, [d]       ; 4th arg
mov r8, [e]        ; 5th arg
mov r9, [f]        ; 6th arg
push [g]           ; 7th arg on stack
call func
```

**Microsoft x64 (Windows)**
```asm
; Arguments: RCX, RDX, R8, R9, then stack
; Shadow space: 32 bytes reserved on stack
; Return: RAX

; Example: func(a, b, c, d, e)
sub rsp, 0x28      ; Shadow space + alignment
mov rcx, [a]       ; 1st arg
mov rdx, [b]       ; 2nd arg
mov r8, [c]        ; 3rd arg
mov r9, [d]        ; 4th arg
mov [rsp+0x20], [e] ; 5th arg on stack
call func
add rsp, 0x28
```

### ARM Assembly Patterns

#### ARM64 (AArch64) Calling Convention
```asm
; Arguments: X0-X7
; Return: X0 (and X1 for 128-bit)
; Frame pointer: X29
; Link register: X30

; Function prologue
stp x29, x30, [sp, #-16]!  ; Save FP and LR
mov x29, sp                 ; Set frame pointer

; Function epilogue
ldp x29, x30, [sp], #16    ; Restore FP and LR
ret
```

#### ARM32 Calling Convention
```asm
; Arguments: R0-R3, then stack
; Return: R0 (and R1 for 64-bit)
; Link register: LR (R14)

; Function prologue
push {fp, lr}
add fp, sp, #4

; Function epilogue
pop {fp, pc}    ; Return by popping PC
`

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Comprehensive patterns and techniques for analyzing compiled binaries, understanding assembly code, and reconstructing program logic.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Binary Analysis Patterns
- Para tarefas relacionadas a binary analysis patterns

## Diretrizes Específicas

