# programming-fundamentals

> Progressive programming fundamentals repository — built primarily in Python, with JavaScript as a secondary language. TypeScript, Java, Go, and Bash are part of the long-term vision but remain future work. Comparing languages is a secondary benefit of this approach, not its goal.

---

# Overview

This repository documents a progressive journey through programming fundamentals, built primarily in **Python**, with **JavaScript** as a secondary language. TypeScript, Java, Go, and Bash are part of the long-term vision for this repository, but work on them has not started yet.

The order in which concepts are introduced follows a single source of truth: [`docs/learning-path.md`](docs/learning-path.md). Every example and exercise in this repository can be traced back to one of the steps defined there.

Each language has its own top-level folder containing two primary subdirectories:

- `fundamentals/` — structured concept study
  
- `exercises/` — practical exercises and challenges
  

Studying the same fundamentals in more than one language is a natural side effect of this approach, and it does help build a deeper understanding of the underlying concepts — Variables, Functions, Loops, Conditionals, Data structures — rather than a single syntax. That said, this is a secondary benefit of progressive learning, not the organizing principle of the repository. The goal is to build solid fundamentals, not to produce a side-by-side language comparison.

## Language Priority

| Status | Languages |
| --- | --- |
| Primary | Python |
| Secondary | JavaScript |
| Future — not yet started | TypeScript, Java, Go, Bash |

Work on the future languages will not begin until Python and JavaScript are consolidated.

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
│   ├── README.md
│   ├── learning-path.md
│   └── study-guide.md
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
| `docs/` | Learning path, navigation guides, and shared study notes |

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
| Python | Completo — 8/8 pasos de `docs/learning-path.md` | 5 ejercicios (3 en `01-intro`, 2 en `02-challenges`) | Lenguaje principal |
| JavaScript | Completo — 8/8 pasos de `docs/learning-path.md` | 5 ejercicios (3 en `01-intro`, 2 en `02-challenges`) | Lenguaje secundario |
| TypeScript | Not yet | 0   | Futuro — sin fecha definida |
| Java | Not yet | 0   | Futuro — sin fecha definida |
| Bash | Not yet | 0   | Futuro — sin fecha definida |
| Go  | Not yet | 0   | Futuro — sin fecha definida |

**Last updated:** *(update this date when you edit the table)*

---

# Ecosystem

Part of the sxiks project ecosystem.

**Type:** Learning

**Domain:** Programming Fundamentals