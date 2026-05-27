import os

# =========================================================
# EduOS Assignment Project Structure Generator
# =========================================================

STUDENT_ID = "YOUR_STUDENT_ID"

project_name = f"EduOS-{STUDENT_ID}"

folders = [
    "docs/screenshots",

    "c_core/include",
    "c_core/src",
    "c_core/obj",
    "c_core/data",
    "c_core/tests",

    "python_scheduler/algorithms",
    "python_scheduler/input",
    "python_scheduler/output",
    "python_scheduler/tests",

    "controller",

    "logs",

    "scripts",

    ".github/workflows"
]

files = {
    "README.md": "# EduOS Project\n",
    
    ".gitignore": """# Compiled C files
*.o
*.out
eduos

# Python
__pycache__/
*.pyc
venv/

# Logs
*.log

# OS files
.DS_Store
Thumbs.db

# VS Code
.vscode/
""",

    "LICENSE": "MIT License\n",

    # =====================================================
    # docs
    # =====================================================

    "docs/report.pdf": "",
    "docs/presentation.pptx": "",
    "docs/simulation_report.json": "{}",

    # =====================================================
    # C CORE
    # =====================================================

    "c_core/Makefile": """all:
\tgcc -Wall -Wextra -pthread -std=c11 src/*.c -o eduos

clean:
\trm -f eduos *.o

race:
\tgcc -DRACE src/thread_manager.c -pthread -o race_demo

fixed:
\tgcc src/thread_manager.c -pthread -o fixed_demo

memcheck:
\tvalgrind --leak-check=full ./eduos
""",

    "c_core/include/eduos.h": """#ifndef EDUOS_H
#define EDUOS_H

typedef struct {
    int pid;
    char name[64];
    int state;
    int priority;
    int burst_time;
    int arrival_time;
    int remaining_time;
    int memory_req_kb;
    int thread_count;
} PCB;

#endif
""",

    "c_core/src/process_manager.c": """#include <stdio.h>

void edu_ps() {
    printf("Displaying process table...\\n");
}
""",

    "c_core/src/thread_manager.c": """#include <stdio.h>

int main() {
    printf("Thread manager running...\\n");
    return 0;
}
""",

    "c_core/src/ipc_module.c": """#include <stdio.h>

void ipc_demo() {
    printf("IPC module demo...\\n");
}
""",

    "c_core/src/logger.c": """#include <stdio.h>

void log_message(const char *msg) {
    printf("[LOG]: %s\\n", msg);
}
""",

    "c_core/src/utils.c": """#include <stdio.h>

void helper() {
    printf("Utility helper\\n");
}
""",

    "c_core/src/main_sim.c": """#include <stdio.h>

int main() {
    printf("EduOS Simulator Started\\n");
    return 0;
}
""",

    "c_core/data/pcb_snapshot.json": "[]",

    "c_core/tests/test_process_manager.c": """#include <assert.h>

int main() {
    return 0;
}
""",

    "c_core/tests/test_threads.c": """int main() { return 0; }""",

    "c_core/tests/test_ipc.c": """int main() { return 0; }""",

    # =====================================================
    # PYTHON SCHEDULER
    # =====================================================

    "python_scheduler/requirements.txt": """matplotlib
pandas
tabulate
rich
""",

    "python_scheduler/scheduler_sim.py": """import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--random', type=int)
    parser.add_argument('--file', type=str)
    parser.add_argument('--quantum', type=int, default=2)

    args = parser.parse_args()

    print("Scheduler Simulator Running...")
    print(args)

if __name__ == "__main__":
    main()
""",

    "python_scheduler/gantt.py": """import matplotlib.pyplot as plt

def draw_gantt():
    print("Drawing Gantt Chart...")
""",

    "python_scheduler/metrics.py": """def calculate_metrics():
    print("Calculating metrics...")
""",

    "python_scheduler/visualizer.py": """def comparison_chart():
    print("Generating comparison chart...")
""",

    "python_scheduler/algorithms/fcfs.py": """def fcfs(processes):
    return []
""",

    "python_scheduler/algorithms/sjf.py": """def sjf(processes):
    return []
""",

    "python_scheduler/algorithms/priority.py": """def priority_scheduling(processes):
    return []
""",

    "python_scheduler/algorithms/round_robin.py": """def round_robin(processes, quantum):
    return []
""",

    "python_scheduler/input/sample_processes.csv": """pid,arrival,burst,priority
1,0,5,2
2,1,3,1
3,2,8,4
""",

    "python_scheduler/input/sample_processes.json": """[
    {"pid": 1, "arrival": 0, "burst": 5, "priority": 2}
]
""",

    "python_scheduler/output/fcfs_results.json": "{}",
    "python_scheduler/output/sjf_results.json": "{}",
    "python_scheduler/output/priority_results.json": "{}",
    "python_scheduler/output/rr_results.json": "{}",
    "python_scheduler/output/comparison_metrics.json": "{}",

    "python_scheduler/tests/test_fcfs.py": """def test_fcfs():
    assert True
""",

    "python_scheduler/tests/test_rr.py": """def test_rr():
    assert True
""",

    "python_scheduler/tests/test_metrics.py": """def test_metrics():
    assert True
""",

    # =====================================================
    # CONTROLLER
    # =====================================================

    "controller/main_controller.py": """import subprocess

def main():
    print("Starting EduOS Controller...")

if __name__ == "__main__":
    main()
""",

    "controller/config.py": """THREAD_POOL_SIZE = 4
""",

    "controller/process_loader.py": """def load_processes():
    return []
""",

    "controller/monitor.py": """def monitor_snapshot():
    print("Monitoring PCB snapshots...")
""",

    # =====================================================
    # LOGS
    # =====================================================

    "logs/eduos.log": "",
    "logs/scheduler.log": "",
    "logs/controller.log": "",

    # =====================================================
    # SCRIPTS
    # =====================================================

    "scripts/build.sh": """#!/bin/bash
echo "Building EduOS..."
""",

    "scripts/run_all.sh": """#!/bin/bash
echo "Running full system..."
""",

    "scripts/run_scheduler.sh": """#!/bin/bash
python3 python_scheduler/scheduler_sim.py
""",

    "scripts/clean.sh": """#!/bin/bash
echo "Cleaning project..."
""",

    # =====================================================
    # GITHUB ACTIONS
    # =====================================================

    ".github/workflows/ci.yml": """name: EduOS CI

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Build C Core
        run: |
          cd c_core
          make
"""
}

# =========================================================
# CREATE PROJECT
# =========================================================

print(f"Creating project structure: {project_name}")

os.makedirs(project_name, exist_ok=True)

# Create folders
for folder in folders:
    path = os.path.join(project_name, folder)
    os.makedirs(path, exist_ok=True)
    print(f"[DIR]  {path}")

# Create files
for file_path, content in files.items():
    full_path = os.path.join(project_name, file_path)

    # Ensure parent directory exists
    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[FILE] {full_path}")

print("\\nEduOS project structure created successfully!")
print(f"Project location: ./{project_name}")