This template is designed to align with your high-frequency development workflow. It ensures that every contribution to the `phystensor` repository meets the "Century-Proof" standards required for **Xylema** and **Ampere©** industrial applications.

---

# **Pull Request Template**

## **Description**
*   **What does this PR do?** (e.g., New unit definition, optimized linalg solver, bug fix in SI-vector math)
*   **Which industrial domain does this affect?** (Maritime / EEE / Agri-Tech / Core)
*   **Related Issue:** (e.g., Fixes #102)

## **Type of Change**
- [ ] **Core SI-Vector Change** (Requires rigorous validation of 7-tuple logic)
- [ ] **New Feature** (New units, constants, or utility functions)
- [ ] **Optimization** (Performance improvements for high-frequency inference)
- [ ] **Bug Fix** (Correcting physical or numerical inaccuracies)
- [ ] **Documentation/Examples** (Updating the showroom or security protocols)

## **Technical Checklist**
- [ ] **Dimensional Integrity:** Verified that all new operations maintain correct SI-base vectors.
- [ ] **NumPy Interop:** Tested with vectorized arrays, not just scalars.
- [ ] **Unit Registry:** If adding units, they are defined in `UNIT_DEFINITIONS` with correct scale factors.
- [ ] **Sterilization:** Any new API-facing logic includes a sterilization layer for raw data.

## **Testing & Benchmarks**
- [ ] **New Tests:** Added relevant tests in the `tests/` folder.
- [ ] **Regression:** All existing tests passed (`pytest tests/`).
- [ ] **Performance:** Ran `benchmarks.py` to ensure no significant overhead was introduced.

## **Industrial Context**
*How does this change benefit the "Low Labor, High Scalable" business model?*
> (e.g., "Reduces computational overhead for real-time CII calculations by 15%")

---

### **Maintainer Notes**
*   **GitHub Streak:** Does this contribution maintain the daily momentum?
*   **Standard over Consensus:** Does this meet the internal "Xylema Standard" for software architecture?

---

### **Final Review Status**
- [ ] Approved for Production
- [ ] Needs Refactoring
- [ ] Rejected (Violates physical or modularity principles)
