#!/bin/bash

# Poll Link Checker Script
# This script scans the repository for any poll-related links and reports them

echo "🔍 Scanning repository for poll links..."
echo "================================================"

# Initialize counters
total_violations=0

# Define poll-related patterns to search for (avoiding false positives like "pollution")
poll_patterns=(
    "https.*\/poll"
    "http.*\/poll"
    "https.*poll\."
    "http.*poll\."
    "\[.*poll.*\]"
    "github\.com.*\/poll"
    "\bpoll\b"
    "poll.*link"
    "link.*poll"
    "\*\*poll\*\*"
    "_poll_"
    "\/poll\/"
)

# Search in markdown files (excluding policy-related files)
echo "📄 Checking markdown files..."
for pattern in "${poll_patterns[@]}"; do
    violations=$(find . -name "*.md" ! -path "./.github/DISCUSSION_POLICY.md" ! -path "./.github/ISSUE_TEMPLATE/*" ! -path "./README.md" -exec grep -il "$pattern" {} \; 2>/dev/null | wc -l)
    if [ $violations -gt 0 ]; then
        echo "❌ Found $violations files with pattern: $pattern"
        find . -name "*.md" ! -path "./.github/DISCUSSION_POLICY.md" ! -path "./.github/ISSUE_TEMPLATE/*" ! -path "./README.md" -exec grep -l "$pattern" {} \; 2>/dev/null
        total_violations=$((total_violations + violations))
    fi
done

# Search in other text files (excluding policy-related files)
echo "📄 Checking other text files..."
for pattern in "${poll_patterns[@]}"; do
    violations=$(find . -type f \( -name "*.txt" -o -name "*.json" -o -name "*.yml" -o -name "*.yaml" \) ! -path "./.github/workflows/poll-link-checker.yml" -exec grep -il "$pattern" {} \; 2>/dev/null | wc -l)
    if [ $violations -gt 0 ]; then
        echo "❌ Found $violations files with pattern: $pattern"
        find . -type f \( -name "*.txt" -o -name "*.json" -o -name "*.yml" -o -name "*.yaml" \) ! -path "./.github/workflows/poll-link-checker.yml" -exec grep -l "$pattern" {} \; 2>/dev/null
        total_violations=$((total_violations + violations))
    fi
done

# Summary
echo "================================================"
if [ $total_violations -eq 0 ]; then
    echo "✅ No poll links found! Repository is compliant."
    exit 0
else
    echo "❌ Found $total_violations potential poll link violations."
    echo "📋 Please review and remove any poll-related content."
    exit 1
fi