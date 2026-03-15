#!/usr/bin/env python3
"""
Agent Skills Validator
Validates SKILL.md files against the official Agent Skills specification.
https://agentskills.io/specification
"""

import os
import re
import sys
import json
import glob

def validate_skill(skill_dir):
    """Validate a single skill directory against the spec."""
    results = {
        "skill_dir": skill_dir,
        "errors": [],
        "warnings": [],
        "passed": []
    }
    
    skill_name = os.path.basename(skill_dir)
    skill_md_path = os.path.join(skill_dir, "SKILL.md")
    
    # Check SKILL.md exists
    if not os.path.exists(skill_md_path):
        results["errors"].append("SKILL.md が見つかりません（必須ファイル）")
        return results
    results["passed"].append("SKILL.md ファイルが存在する")
    
    with open(skill_md_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Parse frontmatter
    fm_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not fm_match:
        results["errors"].append("YAML frontmatter が見つかりません（---で囲む）")
        return results
    results["passed"].append("YAML frontmatter が存在する")
    
    frontmatter = fm_match.group(1)
    end_idx = int(fm_match.end()) # type: ignore
    body = content[end_idx:]
    
    # Validate name field
    name_match = re.search(r'^name:\s*(.+)$', frontmatter, re.MULTILINE)
    if not name_match:
        results["errors"].append("name フィールドが見つかりません（必須）")
    else:
        name = name_match.group(1).strip()
        
        # Name length
        if len(name) < 1 or len(name) > 64:
            results["errors"].append(f"name は1-64文字必要（現在: {len(name)}文字）")
        else:
            results["passed"].append(f"name の長さが適正（{len(name)}文字）")
        
        # Name characters
        if not re.match(r'^[a-z0-9][a-z0-9-]*[a-z0-9]$', name) and len(name) > 1:
            if name.startswith('-') or name.endswith('-'):
                results["errors"].append(f"name はハイフンで始まる・終わることは不可（{name}）")
            elif '--' in name:
                results["errors"].append(f"name に連続ハイフンは不可（{name}）")
            elif not re.match(r'^[a-z0-9-]+$', name):
                results["errors"].append(f"name は小文字英数字とハイフンのみ使用可（{name}）")
        else:
            results["passed"].append(f"name のフォーマットが正しい（{name}）")
        
        # Name matches directory
        if name != skill_name:
            results["errors"].append(f"name（{name}）がディレクトリ名（{skill_name}）と一致しません")
        else:
            results["passed"].append(f"name がディレクトリ名と一致する")
    
    # Validate description field
    desc_match = re.search(r'^description:\s*\|?\s*\n((?:\s+.+\n)*)', frontmatter, re.MULTILINE)
    if not desc_match:
        desc_match2 = re.search(r'^description:\s*(.+)$', frontmatter, re.MULTILINE)
        if not desc_match2:
            results["errors"].append("description フィールドが見つかりません（必須）")
        else:
            desc = desc_match2.group(1).strip()
            if len(desc) < 1 or len(desc) > 1024:
                results["errors"].append(f"description は1-1024文字必要（現在: {len(desc)}文字）")
            else:
                results["passed"].append(f"description の長さが適正（{len(desc)}文字）")
    else:
        desc = desc_match.group(1).strip()
        if len(desc) < 1 or len(desc) > 1024:
            results["errors"].append(f"description は1-1024文字必要（現在: {len(desc)}文字）")
        else:
            results["passed"].append(f"description の長さが適正（{len(desc)}文字）")
    
    # Check body line count
    body_lines = body.strip().split('\n')
    line_count = len(body_lines)
    if line_count > 500:
        results["warnings"].append(f"SKILL.md 本体が500行を超えています（{line_count}行）。references/に分割を推奨")
    else:
        results["passed"].append(f"SKILL.md 本体が500行以内（{line_count}行）")
    
    # Check for examples
    if '## Example' in body or '## example' in body or '**Example' in body:
        results["passed"].append("Examples セクションが存在する")
    else:
        results["warnings"].append("Examples セクションが見つかりません（推奨）")
    
    # Check for edge cases
    if 'Edge Case' in body or 'edge case' in body:
        results["passed"].append("Edge Cases セクションが存在する")
    else:
        results["warnings"].append("Edge Cases セクションが見つかりません（推奨）")
    
    # Check for guidelines
    if '## Guideline' in body or '## guideline' in body:
        results["passed"].append("Guidelines セクションが存在する")
    else:
        results["warnings"].append("Guidelines セクションが見つかりません（推奨）")
    
    # Check evals directory
    evals_path = os.path.join(skill_dir, "evals", "evals.json")
    if os.path.exists(evals_path):
        try:
            with open(evals_path, "r", encoding="utf-8") as f:
                evals = json.load(f)
            eval_count = len(evals.get("evals", []))
            if eval_count >= 2:
                results["passed"].append(f"テストケースが{eval_count}件存在する")
            else:
                results["warnings"].append(f"テストケースが{eval_count}件のみ（2件以上推奨）")
        except json.JSONDecodeError:
            results["errors"].append("evals.json のJSONフォーマットが不正です")
    else:
        results["warnings"].append("evals/evals.json が見つかりません（推奨）")
    
    # Check optional directories
    for dir_name in ["scripts", "references", "assets"]:
        dir_path = os.path.join(skill_dir, dir_name)
        if os.path.exists(dir_path):
            results["passed"].append(f"{dir_name}/ ディレクトリが存在する")
    
    return results


def print_results(results):
    """Print validation results."""
    skill_name = os.path.basename(results["skill_dir"])
    
    print(f"\n{'='*60}")
    print(f"  Skill: {skill_name}")
    print(f"{'='*60}")
    
    if results["passed"]:
        print(f"\n  ✅ PASSED ({len(results['passed'])})")
        for item in results["passed"]:
            print(f"     ✓ {item}")
    
    if results["warnings"]:
        print(f"\n  ⚠️  WARNINGS ({len(results['warnings'])})")
        for item in results["warnings"]:
            print(f"     △ {item}")
    
    if results["errors"]:
        print(f"\n  ❌ ERRORS ({len(results['errors'])})")
        for item in results["errors"]:
            print(f"     ✗ {item}")
    
    # Summary
    total = len(results["passed"]) + len(results["warnings"]) + len(results["errors"])
    if not results["errors"]:
        print(f"\n  🎉 判定: PASS（{len(results['passed'])}/{total}項目クリア）")
    else:
        print(f"\n  💥 判定: FAIL（エラー{len(results['errors'])}件）")
    
    return len(results["errors"]) == 0


def main():
    skills_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    
    print("=" * 60)
    print("  Agent Skills Validator v1.0")
    print("  Based on: https://agentskills.io/specification")
    print("=" * 60)
    
    # Find all skill directories (containing SKILL.md)
    skill_dirs = []
    for root, dirs, files in os.walk(skills_dir):
        if "SKILL.md" in files and "templates" not in root:
            skill_dirs.append(root)
    
    if not skill_dirs:
        print(f"\nNo skills found in {skills_dir}")
        return
    
    print(f"\n{len(skill_dirs)} skill(s) found.\n")
    
    all_passed = True
    for skill_dir in sorted(skill_dirs):
        results = validate_skill(skill_dir)
        passed = print_results(results)
        if not passed:
            all_passed = False
    
    print(f"\n{'='*60}")
    if all_passed:
        print("  ✅ ALL SKILLS PASSED VALIDATION")
    else:
        print("  ❌ SOME SKILLS HAVE ERRORS")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
