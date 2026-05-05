Since you’ve hit a **195+ day streak**, your `CONTRIBUTING.md` needs to reflect that this isn't just a repository—it’s a high-frequency engineering ritual. This document defines the "Xylema Standard" for code quality, modularity, and physical accuracy.

It tells contributors: **"We don't just write code; we build century-proof systems."**

---

# **Contributing to Phystensor**

First, thank you for considering a contribution. **Phystensor** is the foundational engine for **Xylema Private Limited’s** industrial inference services. We value objective technical mastery, modular architecture, and the pursuit of internal excellence over social consensus.

## **The Founder’s Philosophy**
*   **Low Labor, High Scalable:** Every contribution should aim to reduce the marginal cost of the next calculation or the next user.
*   **Century-Proof Architecture:** We decouple physical logic from data ingestion. We favor modularity over convenience.
*   **Physical Integrity:** A bug in a unit conversion is not just a software error; in our domains (Maritime, EEE, Agri-Tech), it is a physical failure.

---

## **How to Contribute**

### **1. High-Frequency Momentum**
We maintain a consistent daily contribution rhythm. If you are working on a large feature, break it into small, atomic, and physically validated PRs.

### **2. The SI-Base Guardrail**
Any change to the core `PhysicalTensor` or `Dimensions` class must be vetted against the **7-tuple SI DNA**. 
*   **Length, Mass, Time, Current, Temperature, Amount, Luminous Intensity.**
*   If your math doesn't reconcile back to these seven, it does not belong in the core.

### **3. Industrial Domain Focus**
We prioritize contributions that solve problems in:
*   **Maritime Compliance:** IMO, CII, and fuel efficiency logic.
*   **Electrical Engineering (EEE):** Load analysis and power systems.
*   **Industrial Agri-Tech:** Thermodynamics for vertical farming.

---

## **Development Standards**

### **Code Style**
*   **Functional & Modular:** Keep functions small. Use the `pt.q()` alias for user-facing examples.
*   **Type Hinting:** Strictly enforced. We use Python’s type system to mirror the physical certainty of our math.
*   **Documentation:** All new units or constants must be cited with their standard source (CODATA, IMO regulations, etc.).

### **Testing Protocol**
No PR will be merged without:
1.  **Unit Tests:** Validating scalar and NumPy array operations.
2.  **Dimensional Tests:** Proving the operation results in the expected SI-vector.
3.  **Zero-Hallucination:** Ensure no units are "guessed" or "estimated."

---

## **Submission Process**
1.  **Fork & Branch:** Create a feature branch.
2.  **Maintain the Streak:** Small, meaningful commits are preferred over massive, monolithic dumps.
3.  **PR Template:** Fill out the `PULL_REQUEST_TEMPLATE.md` in full.
4.  **Security Check:** Ensure no proprietary industrial telemetry or sensitive API keys are included in examples.

---

## **Rewards & Recognition**
We value merit above all else. Significant contributors who demonstrate a deep understanding of **"Inference as a Service"** and century-proof architecture will be recognized within the Xylema ecosystem.

> "Internal standards are the only ones that matter."

---

### **Quick Check before you commit:**
*   Did you use `math.sqrt` instead of `**0.5`? (Use the latter to preserve `PhysicalTensor` logic).
*   Did you add a unit? (Ensure it’s in `UNIT_DEFINITIONS`).
*   Does it break the Maritime performance benchmarks?

**Let’s build something that lasts.**
