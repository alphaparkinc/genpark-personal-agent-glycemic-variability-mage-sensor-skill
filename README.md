# Continuous Glycemic Variability & MAGE Glucose Dynamics Skill

[![GenPark Official](https://img.shields.io/badge/GenPark-Official%20Skill-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-blue)](https://www.linkedin.com/company/92955550)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-green)](https://modelcontextprotocol.io/)
[![Zero Dependency](https://img.shields.io/badge/Dependencies-Zero%20Stdlib-brightgreen)](https://python.org)

Mean Amplitude of Glycemic Excursions (MAGE), Continuous Overall Net Glycemic Action (CONGA), and postprandial glucose spike area under curve (AUC). Built for GenPark (https://www.genpark.ai).

## 🌐 Official Channels
- **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## 🛠️ MCP Tools Exposed
- `calculate_mage_and_conga_variability`: Compute MAGE (Mean Amplitude of Glycemic Excursions) and Standard Deviation across CGM telemetry array.
- `synthesize_postprandial_attenuation_protocol`: Synthesize immediate behavioral and supplement interventions to flatten glucose spike excursion.

## 🚀 Installation & Usage
```bash
python -m genpark_personal_agent_glycemic_variability_mage_sensor_skill.server --test
```
