This document outlines the security protocols for the **phystensor** ecosystem. Given your focus on "Inference as a Service" and the industrial nature of **Xylema Private Limited**, security isn't just about protecting code—it's about ensuring the physical integrity of the data used in global maritime and engineering operations.

---

## **Security Policy: Phystensor Ecosystem**

### **1. The "Physical Integrity" Mandate**
In industrial physics, a data error is a security vulnerability. 
*   **Dimensional Sterilization:** All external data entering the system via API must be "sterilized" into `PhysicalTensor` objects. This prevents **Unit Injection Attacks**, where mismatched units could lead to catastrophic failures in downstream industrial control systems.
*   **Zero-Guessing Policy:** The engine will never "guess" a unit. If a calculation is dimensionally ambiguous, the system must raise a `DimensionalityError` and halt execution rather than providing an incorrect physical result.

---

### **2. Software Supply Chain**
*   **Dependency Minimization:** To maintain a "Century-Proof" architecture, `phystensor` aims for near-zero dependencies beyond **NumPy**. This reduces the attack surface for supply chain vulnerabilities.
*   **GitHub Streak & Audit:** Every commit in the 195+ day contribution streak is signed and reviewed to ensure no malicious logic is introduced into the core SI-vector math.

---

### **3. Reporting Vulnerabilities**
We value objective mastery and rigorous standards. If you discover a security flaw—be it a logic error in the dimension vectors or a standard software exploit—please report it through the following channels:

*   **Lead Maintainer:** Contact the Founder/Managing Director of Xylema Private Limited directly.
*   **Preferred Method:** Open a GitHub Issue labeled `security` or send an encrypted message via the corporate portal.

> **Note:** We care more about meeting internal safety standards than public optics. All valid security reports will be addressed with high-frequency updates.

---

### **4. Safe Operating Practices**
*   **API Exposure:** When deploying `phystensor` as a service, always use a **Sterilization Layer** (as demonstrated in `examples/05_api_sterilization.py`) to validate inbound JSON payloads.
*   **Execution Environment:** While `phystensor` itself is a mathematical library, it should be run in isolated environments (Docker/Podman) when handling unverified telemetry from third-party maritime sensors.
*   **Industrial Guardrails:** Always wrap critical power (EEE) or thermal (Agri-tech) calculations in `try-except` blocks to handle `PhystensorError`. A caught exception is a prevented industrial accident.

---

### **5. Data Privacy (Inference as a Service)**
*   **Stateless Inference:** The core engine does not store user data. It processes inputs into physical outputs and clears the tensor buffers immediately.
*   **Local-First:** For sensitive maritime trade routes or proprietary mushroom cultivation formulas, we recommend running the engine locally or within a private cloud instance to ensure data residency.

---
