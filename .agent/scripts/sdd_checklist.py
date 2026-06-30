#!/usr/bin/env python3
"""
SDD Checklist Runner -  Spec-Driven Development
=======================================================

Validação completa para desenvolvimento guiado por especificações.
Inclui Gates Constitucionais do .

Usage:
    python .agent/scripts/sdd_checklist.py .                    # Run all checks
    python .agent/scripts/sdd_checklist.py . --gates-only       # Only constitutional gates
    python .agent/scripts/sdd_checklist.py . --security-only    # Only security checks
    python .agent/scripts/sdd_checklist.py . --spec specs/001   # Validate specific spec

Priority Order:
    P0: Constitutional Gates (must pass)
    P1: Security Scan (vulnerabilities, secrets)
    P2: Lint & Type Check (code quality)
    P3: Spec Validation (SDD compliance)
    P4: Test Runner (unit/integration tests)
    P5: Performance (if URL provided)
"""

import argparse
import subprocess
import sys
from pathlib import Path
from dataclasses import dataclass
from enum import Enum
from typing import Optional


class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


class GateStatus(Enum):
    PASS = "pass"
    FAIL = "fail"
    WARN = "warn"
    SKIP = "skip"


@dataclass
class GateResult:
    name: str
    status: GateStatus
    message: str
    details: list[str]


def print_header(text: str) -> None:
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*70}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}{text.center(70)}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*70}{Colors.ENDC}\n")


def print_section(text: str) -> None:
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'─'*70}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.BLUE}  {text}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'─'*70}{Colors.ENDC}\n")


def print_gate(name: str, status: GateStatus, message: str = "") -> None:
    icons = {
        GateStatus.PASS: f"{Colors.GREEN}✅",
        GateStatus.FAIL: f"{Colors.RED}❌",
        GateStatus.WARN: f"{Colors.YELLOW}⚠️",
        GateStatus.SKIP: f"{Colors.CYAN}⏭️",
    }
    icon = icons.get(status, "❓")
    print(f"{icon} {name}{Colors.ENDC}")
    if message:
        print(f"   {message}")


def print_success(text: str) -> None:
    print(f"{Colors.GREEN}✅ {text}{Colors.ENDC}")


def print_warning(text: str) -> None:
    print(f"{Colors.YELLOW}⚠️  {text}{Colors.ENDC}")


def print_error(text: str) -> None:
    print(f"{Colors.RED}❌ {text}{Colors.ENDC}")


# =============================================================================
# CONSTITUTIONAL GATES
# =============================================================================

class ConstitutionalGates:
    """Validates compliance with  Constitution"""
    
    ARTICLES = {
        "I": "Library-First Principle",
        "II": "CLI Interface Mandate", 
        "III": "Test-First Imperative",
        "VII": "Simplicity Gate",
        "VIII": "Anti-Abstraction Gate",
        "IX": "Integration-First Testing",
        "X": "Security Foundation",
    }
    
    def __init__(self, project_path: Path):
        self.project_path = project_path
        self.results: list[GateResult] = []
    
    def run_all(self) -> list[GateResult]:
        """Execute all constitutional gates"""
        print_section("🏛️  CONSTITUTIONAL GATES")
        
        self.gate_simplicity()
        self.gate_anti_abstraction()
        self.gate_test_first()
        self.gate_integration_first()
        self.gate_library_first()
        self.gate_security()
        
        return self.results
    
    def gate_simplicity(self) -> None:
        """Article VII: Maximum 3 projects"""
        pyproject_files = list(self.project_path.rglob("pyproject.toml"))
        project_count = len(pyproject_files)
        
        if project_count <= 3:
            result = GateResult(
                name="Gate de Simplicidade (Artigo VII)",
                status=GateStatus.PASS,
                message=f"Usando {project_count} projeto(s) (≤3)",
                details=[str(p.relative_to(self.project_path)) for p in pyproject_files]
            )
        else:
            result = GateResult(
                name="Gate de Simplicidade (Artigo VII)",
                status=GateStatus.FAIL,
                message=f"Usando {project_count} projetos (>3) - requer justificativa",
                details=[str(p.relative_to(self.project_path)) for p in pyproject_files]
            )
        
        self.results.append(result)
        print_gate(result.name, result.status, result.message)
    
    def gate_anti_abstraction(self) -> None:
        """Article VIII: No unnecessary abstractions"""
        issues = []
        
        # Check for common over-abstractions
        patterns_to_check = [
            ("**/*repository*.py", "Repository pattern - verificar necessidade"),
            ("**/*factory*.py", "Factory pattern - verificar necessidade"),
            ("**/*manager*.py", "Manager classes - verificar se framework não resolve"),
        ]
        
        for pattern, warning in patterns_to_check:
            matches = list(self.project_path.glob(pattern))
            if matches:
                issues.append(f"{warning}: {len(matches)} arquivo(s)")
        
        if not issues:
            result = GateResult(
                name="Gate Anti-Abstração (Artigo VIII)",
                status=GateStatus.PASS,
                message="Sem abstrações desnecessárias detectadas",
                details=[]
            )
        else:
            result = GateResult(
                name="Gate Anti-Abstração (Artigo VIII)",
                status=GateStatus.WARN,
                message="Abstrações detectadas - verificar necessidade",
                details=issues
            )
        
        self.results.append(result)
        print_gate(result.name, result.status, result.message)
        for detail in result.details:
            print(f"   • {detail}")
    
    def gate_test_first(self) -> None:
        """Article III: Tests before implementation"""
        src_dir = self.project_path / "src"
        tests_dir = self.project_path / "tests"
        
        if not tests_dir.exists():
            result = GateResult(
                name="Gate Test-First (Artigo III)",
                status=GateStatus.FAIL,
                message="Diretório tests/ não encontrado",
                details=[]
            )
        else:
            test_files = list(tests_dir.rglob("test_*.py"))
            src_files = list(src_dir.rglob("*.py")) if src_dir.exists() else []
            
            if test_files:
                result = GateResult(
                    name="Gate Test-First (Artigo III)",
                    status=GateStatus.PASS,
                    message=f"{len(test_files)} arquivo(s) de teste encontrado(s)",
                    details=[]
                )
            else:
                result = GateResult(
                    name="Gate Test-First (Artigo III)",
                    status=GateStatus.FAIL,
                    message="Nenhum arquivo de teste encontrado",
                    details=[]
                )
        
        self.results.append(result)
        print_gate(result.name, result.status, result.message)
    
    def gate_integration_first(self) -> None:
        """Article IX: Prefer real databases over mocks"""
        tests_dir = self.project_path / "tests"
        integration_dir = tests_dir / "integration"
        
        if integration_dir.exists() and list(integration_dir.glob("*.py")):
            result = GateResult(
                name="Gate Integration-First (Artigo IX)",
                status=GateStatus.PASS,
                message="Diretório tests/integration/ encontrado",
                details=[]
            )
        else:
            result = GateResult(
                name="Gate Integration-First (Artigo IX)",
                status=GateStatus.WARN,
                message="tests/integration/ não encontrado - criar testes de integração",
                details=[]
            )
        
        self.results.append(result)
        print_gate(result.name, result.status, result.message)
    
    def gate_library_first(self) -> None:
        """Article I: Features as libraries"""
        src_dir = self.project_path / "src"
        
        # Check for CLI structure
        cli_dir = src_dir / "cli"
        has_cli = cli_dir.exists() and list(cli_dir.glob("*.py"))
        
        if has_cli:
            result = GateResult(
                name="Gate Library-First (Artigo I)",
                status=GateStatus.PASS,
                message="Interface CLI encontrada em src/cli/",
                details=[]
            )
        else:
            result = GateResult(
                name="Gate Library-First (Artigo I)",
                status=GateStatus.WARN,
                message="src/cli/ não encontrado - considerar exposição via CLI",
                details=[]
            )
        
        self.results.append(result)
        print_gate(result.name, result.status, result.message)
    
    def gate_security(self) -> None:
        """Article X: Security as foundation"""
        issues = []
        
        # Check for .env files
        env_files = list(self.project_path.glob(".env*"))
        env_in_gitignore = False
        
        gitignore = self.project_path / ".gitignore"
        if gitignore.exists():
            content = gitignore.read_text()
            env_in_gitignore = ".env" in content or "*.env" in content
        
        if env_files and not env_in_gitignore:
            issues.append("Arquivos .env podem não estar no .gitignore")
        
        # Check for secrets in code (basic patterns)
        secret_patterns = ["password", "secret", "token", "key"]
        py_files = list(self.project_path.rglob("*.py"))
        
        for py_file in py_files[:20]:  # Check first 20 files
            try:
                content = py_file.read_text()
                for pattern in secret_patterns:
                    if f'{pattern} = "' in content.lower() or f"{pattern} = '" in content.lower():
                        if "os.environ" not in content and "getenv" not in content:
                            issues.append(f"Possível hardcoded secret em {py_file.name}")
                            break
            except Exception:
                pass
        
        if not issues:
            result = GateResult(
                name="Gate de Segurança (Artigo X)",
                status=GateStatus.PASS,
                message="Nenhum problema de segurança óbvio detectado",
                details=[]
            )
        else:
            result = GateResult(
                name="Gate de Segurança (Artigo X)",
                status=GateStatus.FAIL,
                message="Problemas de segurança detectados",
                details=issues[:5]  # Limit to 5 issues
            )
        
        self.results.append(result)
        print_gate(result.name, result.status, result.message)
        for detail in result.details:
            print(f"   • {detail}")


# =============================================================================
# SPEC VALIDATION
# =============================================================================

class SpecValidator:
    """Validates SDD specification files"""
    
    def __init__(self, project_path: Path):
        self.project_path = project_path
    
    def validate_spec(self, spec_path: Path) -> list[GateResult]:
        """Validate a single spec file"""
        results = []
        
        if not spec_path.exists():
            return [GateResult(
                name="Spec Validation",
                status=GateStatus.FAIL,
                message=f"Spec não encontrado: {spec_path}",
                details=[]
            )]
        
        content = spec_path.read_text()
        
        # Check required sections
        required_sections = [
            ("🎯 Visão Geral", "Visão Geral"),
            ("👤 User Stories", "User Stories"),
            ("📋 Requisitos", "Requisitos"),
            ("✅ Critérios de Sucesso", "Critérios de Sucesso"),
        ]
        
        for marker, name in required_sections:
            if marker in content:
                results.append(GateResult(
                    name=f"Seção: {name}",
                    status=GateStatus.PASS,
                    message="Seção encontrada",
                    details=[]
                ))
            else:
                results.append(GateResult(
                    name=f"Seção: {name}",
                    status=GateStatus.FAIL,
                    message="Seção não encontrada",
                    details=[]
                ))
        
        # Check for clarification markers
        if "[NEEDS CLARIFICATION" in content:
            results.append(GateResult(
                name="Clarificações Pendentes",
                status=GateStatus.WARN,
                message="Marcadores [NEEDS CLARIFICATION] encontrados na spec",
                details=[]
            ))
        
        return results
    
    def validate_all_specs(self) -> list[GateResult]:
        """Validate all specs in specs/ directory"""
        specs_dir = self.project_path / "specs"
        results = []
        
        if not specs_dir.exists():
            return [GateResult(
                name="Specs Directory",
                status=GateStatus.SKIP,
                message="Diretório specs/ não encontrado",
                details=[]
            )]
        
        spec_dirs = [d for d in specs_dir.iterdir() if d.is_dir()]
        
        if not spec_dirs:
            return [GateResult(
                name="Specs",
                status=GateStatus.SKIP,
                message="Nenhuma spec encontrada em specs/",
                details=[]
            )]
        
        for spec_dir in spec_dirs:
            spec_file = spec_dir / "spec.md"
            if spec_file.exists():
                spec_results = self.validate_spec(spec_file)
                results.extend(spec_results)
        
        return results


# =============================================================================
# SECURITY SCAN
# =============================================================================

def run_security_scan(project_path: Path) -> GateResult:
    """Run security scan using detect-secrets and basic checks"""
    issues = []
    
    # Check for detect-secrets
    try:
        result = subprocess.run(
            ["detect-secrets", "scan", str(project_path)],
            capture_output=True,
            text=True,
            timeout=60
        )
        if result.returncode != 0:
            issues.append("detect-secrets encontrou potenciais secrets")
    except FileNotFoundError:
        issues.append("detect-secrets não instalado")
    except Exception as e:
        issues.append(f"Erro ao executar detect-secrets: {e}")
    
    # Check pre-commit
    precommit_config = project_path / ".pre-commit-config.yaml"
    if not precommit_config.exists():
        issues.append(".pre-commit-config.yaml não encontrado")
    
    if not issues:
        return GateResult(
            name="Security Scan",
            status=GateStatus.PASS,
            message="Nenhum problema de segurança detectado",
            details=[]
        )
    else:
        return GateResult(
            name="Security Scan",
            status=GateStatus.WARN,
            message="Verificações de segurança incompletas",
            details=issues
        )


# =============================================================================
# CODE QUALITY
# =============================================================================

def run_lint_check(project_path: Path) -> GateResult:
    """Run ruff lint check"""
    try:
        result = subprocess.run(
            ["uv", "run", "ruff", "check", "."],
            cwd=project_path,
            capture_output=True,
            text=True,
            timeout=120
        )
        
        if result.returncode == 0:
            return GateResult(
                name="Lint Check (ruff)",
                status=GateStatus.PASS,
                message="Nenhum problema de lint encontrado",
                details=[]
            )
        else:
            lines = result.stdout.strip().split("\n")
            return GateResult(
                name="Lint Check (ruff)",
                status=GateStatus.FAIL,
                message=f"{len(lines)} problema(s) de lint encontrado(s)",
                details=lines[:5]
            )
    except FileNotFoundError:
        return GateResult(
            name="Lint Check (ruff)",
            status=GateStatus.SKIP,
            message="ruff não encontrado",
            details=[]
        )
    except Exception as e:
        return GateResult(
            name="Lint Check (ruff)",
            status=GateStatus.FAIL,
            message=f"Erro: {e}",
            details=[]
        )


def run_type_check(project_path: Path) -> GateResult:
    """Run mypy type check"""
    try:
        result = subprocess.run(
            ["uv", "run", "mypy", "."],
            cwd=project_path,
            capture_output=True,
            text=True,
            timeout=120
        )
        
        if result.returncode == 0:
            return GateResult(
                name="Type Check (mypy)",
                status=GateStatus.PASS,
                message="Type checking passou",
                details=[]
            )
        else:
            return GateResult(
                name="Type Check (mypy)",
                status=GateStatus.WARN,
                message="Problemas de tipo encontrados (verificar se críticos)",
                details=result.stdout.strip().split("\n")[:5]
            )
    except FileNotFoundError:
        return GateResult(
            name="Type Check (mypy)",
            status=GateStatus.SKIP,
            message="mypy não encontrado",
            details=[]
        )
    except Exception as e:
        return GateResult(
            name="Type Check (mypy)",
            status=GateStatus.FAIL,
            message=f"Erro: {e}",
            details=[]
        )


# =============================================================================
# TEST RUNNER
# =============================================================================

def run_tests(project_path: Path) -> GateResult:
    """Run pytest"""
    try:
        result = subprocess.run(
            ["uv", "run", "pytest", "-xvs", "--tb=short"],
            cwd=project_path,
            capture_output=True,
            text=True,
            timeout=300
        )
        
        if result.returncode == 0:
            return GateResult(
                name="Test Runner (pytest)",
                status=GateStatus.PASS,
                message="Todos os testes passaram",
                details=[]
            )
        else:
            return GateResult(
                name="Test Runner (pytest)",
                status=GateStatus.FAIL,
                message="Alguns testes falharam",
                details=result.stdout.strip().split("\n")[-10:]
            )
    except FileNotFoundError:
        return GateResult(
            name="Test Runner (pytest)",
            status=GateStatus.SKIP,
            message="pytest não encontrado",
            details=[]
        )
    except Exception as e:
        return GateResult(
            name="Test Runner (pytest)",
            status=GateStatus.FAIL,
            message=f"Erro: {e}",
            details=[]
        )


# =============================================================================
# MAIN
# =============================================================================

def print_summary(results: list[GateResult]) -> bool:
    """Print final summary"""
    print_header("📊 RESUMO DOS CHECKS")
    
    passed = sum(1 for r in results if r.status == GateStatus.PASS)
    failed = sum(1 for r in results if r.status == GateStatus.FAIL)
    warnings = sum(1 for r in results if r.status == GateStatus.WARN)
    skipped = sum(1 for r in results if r.status == GateStatus.SKIP)
    
    print(f"Total: {len(results)} checks")
    print(f"{Colors.GREEN}✅ Passaram: {passed}{Colors.ENDC}")
    print(f"{Colors.RED}❌ Falharam: {failed}{Colors.ENDC}")
    print(f"{Colors.YELLOW}⚠️  Avisos: {warnings}{Colors.ENDC}")
    print(f"{Colors.CYAN}⏭️  Pulados: {skipped}{Colors.ENDC}")
    print()
    
    if failed > 0:
        print_error(f"{failed} gate(s) CRÍTICO(S) falharam - Corrija antes de prosseguir")
        return False
    elif warnings > 0:
        print_warning(f"{warnings} aviso(s) - Recomendado revisar")
        return True
    else:
        print_success("Todos os gates passaram! ✨")
        return True


def main():
    parser = argparse.ArgumentParser(
        description="SDD Checklist -  Spec-Driven Development",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  python .agent/scripts/sdd_checklist.py .                    # Todos os checks
  python .agent/scripts/sdd_checklist.py . --gates-only       # Apenas gates constitucionais
  python .agent/scripts/sdd_checklist.py . --security-only    # Apenas segurança
  python .agent/scripts/sdd_checklist.py . --spec specs/001   # Validar spec específica
        """
    )
    parser.add_argument("project", help="Caminho do projeto")
    parser.add_argument("--gates-only", action="store_true", help="Apenas gates constitucionais")
    parser.add_argument("--security-only", action="store_true", help="Apenas checks de segurança")
    parser.add_argument("--spec", help="Validar spec específica (caminho)")
    parser.add_argument("--skip-tests", action="store_true", help="Pular execução de testes")
    
    args = parser.parse_args()
    
    project_path = Path(args.project).resolve()
    
    if not project_path.exists():
        print_error(f"Caminho do projeto não existe: {project_path}")
        sys.exit(1)
    
    print_header("🚀  SDD CHECKLIST")
    print(f"Projeto: {project_path}")
    print()
    
    all_results: list[GateResult] = []
    
    # Constitutional Gates (always run unless security-only)
    if not args.security_only:
        gates = ConstitutionalGates(project_path)
        gate_results = gates.run_all()
        all_results.extend(gate_results)
        
        # Stop if gates-only
        if args.gates_only:
            all_passed = print_summary(all_results)
            sys.exit(0 if all_passed else 1)
    
    # Security Scan
    if args.security_only or not args.gates_only:
        print_section("🔒 SECURITY SCAN")
        security_result = run_security_scan(project_path)
        all_results.append(security_result)
        print_gate(security_result.name, security_result.status, security_result.message)
        
        if args.security_only:
            all_passed = print_summary(all_results)
            sys.exit(0 if all_passed else 1)
    
    # Spec Validation
    if args.spec:
        print_section("📋 SPEC VALIDATION")
        validator = SpecValidator(project_path)
        spec_path = Path(args.spec)
        if not spec_path.is_absolute():
            spec_path = project_path / spec_path
        spec_results = validator.validate_spec(spec_path)
        all_results.extend(spec_results)
        for r in spec_results:
            print_gate(r.name, r.status, r.message)
    else:
        print_section("📋 SPECS VALIDATION")
        validator = SpecValidator(project_path)
        spec_results = validator.validate_all_specs()
        all_results.extend(spec_results)
        for r in spec_results:
            print_gate(r.name, r.status, r.message)
    
    # Code Quality
    print_section("🛠️  CODE QUALITY")
    lint_result = run_lint_check(project_path)
    all_results.append(lint_result)
    print_gate(lint_result.name, lint_result.status, lint_result.message)
    
    type_result = run_type_check(project_path)
    all_results.append(type_result)
    print_gate(type_result.name, type_result.status, type_result.message)
    
    # Tests
    if not args.skip_tests:
        print_section("🧪 TESTS")
        test_result = run_tests(project_path)
        all_results.append(test_result)
        print_gate(test_result.name, test_result.status, test_result.message)
    
    # Summary
    all_passed = print_summary(all_results)
    
    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
