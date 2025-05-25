Title: Concurrency  
Date: 2025-05-23  
Category: Programming  
Tags: Concurrent, thread  
Summary: Summary about the differences between threads, processes, and programs, with a focus on concurrency threading.

---

**Concurrency** refers to the ability of a system to process multiple tasks or threads over the same period. It improves a program's performance and responsiveness by efficiently managing time and system resources.

Although concurrency allows multitasking, it doesn't always mean true parallel execution. Instead, it often involves **task switching** — doing part of one task, then switching to another, and repeating this cycle until all tasks are complete. This is how most concurrent systems work unless multiple cores are explicitly utilized.

---

## What is a Thread, Process, and Program?

- **Program**: A static set of instructions saved on disk — not yet running.
- **Process**: A program in execution. Each process has its own memory space.
- **Thread**: The smallest unit of execution within a process. Threads within the same process share memory.

> **In C++, we can achieve concurrency using threads.**

---

## Errors and Risks in Concurrency

- **Deadlock**: Occurs when two or more threads are each waiting on resources held by the other, resulting in an indefinite wait.
- **Race Condition**: Happens when threads access shared data at the same time without proper synchronization, leading to unpredictable results.

---

## Synchronization Mechanisms

- **Mutex**: Stands for *mutual exclusion*. It ensures that only one thread can access a critical section (shared resource) at a time. In embedded systems, this is often referred to as a `CRITICAL_SECTION`.

- **Semaphore**: A signaling mechanism that allows a limited number of threads to access a shared resource. If the access count exceeds the allowed limit, additional threads are blocked until it becomes available.

---

## Example: Demonstrating a Race Condition

```cpp
#include <bits/stdc++.h>
#include <mutex>
using namespace std;

long counter = 100; // Shared variable
mutex lck;

void run_concurrent()
{
    // Mutex lock disabled to show race condition
    // lock_guard<mutex> mu(lck);

    for (long i = 0; i < 100000; i++) {
        counter++;
    }

    // mu object would automatically release the lock
}

int main()
{
    thread t1(run_concurrent);
    thread t2(run_concurrent);

    t1.join();
    t2.join();

    cout << "Sum: " << counter << endl;
    return 0;
}
