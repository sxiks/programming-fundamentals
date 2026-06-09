# programming-fundamentals

> Multi-language programming fundamentals repository — exercises and core concepts in Python, JavaScript, TypeScript, Java, Go, and Bash, organized for progressive learning across the sxiks ecosystem.

## Repository Rename Required

This repository was originally created as `programing-fundamentals` (missing one `m`).

The correct name is:

```text
programming-fundamentals
```

See the [Repository Rename](#repository-rename) section for the complete migration procedure.

---

# Overview

This repository documents the learning journey through programming fundamentals across multiple languages.

Each language has its own top-level folder containing two primary subdirectories:

- `fundamentals/` — structured concept study
  
- `exercises/` — practical exercises and challenges
  

The multi-language approach is intentional. Studying the same concepts across different languages helps build a deeper understanding of:

- Variables
  
- Functions
  
- Loops
  
- Conditionals
  
- Data structures
  

Rather than learning a single syntax, the learner develops an understanding of the underlying programming concepts.

This repository is a **learning repository**, not a template.

Its purpose is to:

- Document practice
  
- Track learning progress
  
- Serve as a personal programming reference
  
- Grow throughout the SENA formation process and beyond
  

---

# Learning Objectives

By working through this repository, you will be able to:

- **Write programs in Python**
  
  - Syntax
    
  - Data types
    
  - Functions
    
  - Modules
    
  - Standard library usage
    
- **Write programs in JavaScript**
  
  - Variables
    
  - Functions
    
  - DOM interaction
    
  - Async patterns
    
  - ES6+ syntax
    
- **Understand TypeScript compilation**
  
  - Static typing
    
  - Interfaces
    
  - Types
    
  - Safe development practices
    
- **Understand Object-Oriented Programming in Java**
  
  - Classes
    
  - Inheritance
    
  - Polymorphism
    
  - Encapsulation
    
- **Write efficient tools in Go**
  
  - Static typing
    
  - Compilation
    
  - Concurrency basics
    
  - Fast execution routines
    
- **Automate tasks with Bash**
  
  - Scripting
    
  - Pipes
    
  - Redirects
    
  - Environment variables
    
  - System automation
    
- **Compare programming paradigms**
  
  - Interpreted vs compiled
    
  - Dynamic vs static typing
    
  - Functional vs OOP approaches
    

---

# Skills Developed

| Skill | Folder | Target Languages | Level |
| --- | --- | --- | --- |
| Scripting & Automation | `bash/` | Bash | Beginner |
| Dynamic General Purpose | `python/`, `javascript/` | Python, JavaScript | Beginner–Intermediate |
| Typed Application Development | `typescript/`, `java/`, `go/` | TypeScript, Java, Go | Intermediate |
| Multi-language Git Workflow | All | Markdown, Git, Bash | General |

---

# Repository Structure

```text
programming-fundamentals/
├── bash/
│   ├── exercises/
│   └── fundamentals/
│
├── go/
│   ├── exercises/
│   └── fundamentals/
│
├── java/
│   ├── exercises/
│   └── fundamentals/
│
├── javascript/
│   ├── exercises/
│   └── fundamentals/
│
├── python/
│   ├── exercises/
│   └── fundamentals/
│
├── typescript/
│   ├── exercises/
│   └── fundamentals/
│
├── docs/
│   └── architecture-notes.md
│
└── README.md
```

### Directory Responsibilities

| Directory | Purpose |
| --- | --- |
| `bash/` | Automation and system scripting |
| `go/` | Systems programming and performance-oriented development |
| `java/` | Enterprise object-oriented programming |
| `javascript/` | Interactive web runtime programming |
| `python/` | High-level scripting and application development |
| `typescript/` | Type-safe application development |
| `docs/` | Shared architecture and study notes |

---

# Learning Roadmap

You can study languages in parallel or sequentially.

The recommended progression balances practical value with long-term systems understanding.

```text
Phase 1 — Dynamic Core (Python & JavaScript)
↓
Learn:
- Syntax
- Conditional logic
- Loops
- Basic operations
- Array manipulation

Why:
- Instant feedback
- High visibility
- Foundation for frontend development and scripting

Phase 2 — System Foundations (Bash & Go)
↓
Learn:
- Command automation
- Compilation mechanics
- Pointer mechanics
- Static typing

Why:
- Understand how computers run code
- Handle OS pipelines
- Build efficient tools

Phase 3 — Enterprise Scale (TypeScript & Java)
↓
Learn:
- Interfaces
- Compilation boundaries
- Abstract classes
- OOP patterns

Why:
- Preparation for enterprise frameworks
- Spring Boot
- Angular
- NestJS
```

---

# Folder Architecture Rules

Every language folder must follow the same structure.

```text
[language]/
├── fundamentals/
│   ├── 01-variables.[ext]
│   ├── 02-conditionals.[ext]
│   ├── 03-loops.[ext]
│   └── 04-functions.[ext]
│
└── exercises/
    ├── 01-intro/
    │   └── README.md
    └── 02-challenges/
```

Where:

```text
[ext]
```

matches the language:

| Language | Extension |
| --- | --- |
| Python | `.py` |
| JavaScript | `.js` |
| TypeScript | `.ts` |
| Java | `.java` |
| Go  | `.go` |
| Bash | `.sh` |

---

# Technical Setup Reference

## Python

### Version

```text
Python 3.10+
```

### Run

```bash
python3 python/fundamentals/01-variables.py
```

---

## JavaScript

### Version

```text
Node.js 18+ (LTS)
```

### Run

```bash
node javascript/fundamentals/01-variables.js
```

---

## TypeScript

### Version

```text
TypeScript 5.0+
```

### Installation and Execution

```bash
npm install -g ts-node typescript

ts-node typescript/fundamentals/01-variables.ts
```

---

## Java

### Version

```text
OpenJDK 17
```

### Compile and Execute

```bash
javac java/fundamentals/Variables.java

java java.fundamentals.Variables
```

---

## Go

### Version

```text
Go 1.20+
```

### Run

```bash
go run go/fundamentals/01-variables.go
```

---

## Bash

### Environment

```text
Bash 4.0+
```

### Run

```bash
chmod +x bash/fundamentals/01-variables.sh

./bash/fundamentals/01-variables.sh
```

---

# Repository Rename

This repository was mistakenly created with the name:

```text
programing-fundamentals
```

The correct name is:

```text
programming-fundamentals
```

to comply with ecosystem naming standards.

## Step-by-Step Rename Execution Instructions

Follow these exact commands.

### 1. Navigate to the Local Repository

```bash
cd ~/path/to/your/projects/programing-fundamentals
```

### 2. Rename the GitHub Repository

Open GitHub:

1. Go to repository settings.
  
2. Scroll to the Danger Zone section.
  
3. Rename the repository to:
  

```text
programming-fundamentals
```

### 3. Update the Local Remote URL

Replace the username with your own GitHub username.

```bash
git remote set-url origin https://github.com/your-github-username/programming-fundamentals.git
```

### 4. Verify the Change

```bash
git remote -v
```

### 5. Rename the Local Folder (Optional)

```bash
cd ..

mv programing-fundamentals programming-fundamentals

cd programming-fundamentals
```

---

# Shared References

## Multi-Paradigm Programming

- Exercism – Code Practice Platforms
  
- LeetCode – Algorithmic Challenges
  

## Python

- Python Official Documentation
  
- Real Python Tutorials
  
- Python Tutor – Visualize Code Execution
  

## JavaScript

- MDN JavaScript Guide
  
- javascript.info – The Modern JavaScript Tutorial
  

## TypeScript

- TypeScript Official Docs
  
- TypeScript Deep Dive – Basarat Ali Syed
  

## Java

- Oracle Java Tutorials
  
- Baeldung Java Guides
  

## Go

- Go Official Tour
  
- Go Documentation
  

## Bash

- Bash Manual – GNU
  
- Bash Scripting Tutorial
  

---

# Progress Tracking

| Language | Fundamentals Started | Exercises Done | Notes |
| --- | --- | --- | --- |
| Python | Planned | 2 exercises completed | Fundamentals structure pending |
| JavaScript | Started | 4 exercises (01-intro) | More chapters to add |
| TypeScript | Not yet | 0   | After JavaScript is solid |
| Java | Not yet | 0   | Planned for SENA Java module |
| Bash | Not yet | 0   | Planned for Linux/DevOps module |
| Go  | Not yet | 0   | Future phase |

**Last updated:** *(update this date when you edit the table)*

---

# Ecosystem

Part of the sxiks project ecosystem.

**Type:** Learning

**Domain:** Programming Fundamentals