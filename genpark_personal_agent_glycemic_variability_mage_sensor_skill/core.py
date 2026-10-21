# -*- coding: utf-8 -*-
"""Continuous Glycemic Variability & MAGE Sensor for GenPark Personal Agent."""
import json
import math
from typing import Dict, Any, List

class ContinuousGlycemicVariabilityMAGESensor:
    @staticmethod
    def calculate_mage_and_conga_variability(glucose_readings_mg_dl: List[float], sampling_interval_minutes: int = 5) -> Dict[str, Any]:
        if not glucose_readings_mg_dl:
            return {"error": "Empty glucose reading series."}
        
        n = len(glucose_readings_mg_dl)
        mean_g = sum(glucose_readings_mg_dl) / n
        variance = sum((x - mean_g) ** 2 for x in glucose_readings_mg_dl) / n
        std_g = math.sqrt(variance)
        
        # MAGE calculates excursions exceeding 1 standard deviation
        excursions = []
        for i in range(1, n):
            delta = abs(glucose_readings_mg_dl[i] - glucose_readings_mg_dl[i-1])
            if delta > std_g:
                excursions.append(delta)
        
        mage = round(sum(excursions) / max(1, len(excursions)), 1) if excursions else round(std_g, 1)
        cv_pct = round((std_g / max(1.0, mean_g)) * 100.0, 1)
        
        tier = "OPTIMAL_STABILITY" if cv_pct < 20.0 and mage < 40.0 else ("MODERATE_VARIABILITY" if cv_pct < 36.0 else "HIGH_EXCURSION_RISK")
        return {
            "readings_count": n,
            "mean_glucose_mg_dl": round(mean_g, 1),
            "std_deviation_mg_dl": round(std_g, 1),
            "coefficient_of_variation_cv_pct": cv_pct,
            "mage_score": mage,
            "metabolic_stability_tier": tier
        }

    @staticmethod
    def synthesize_postprandial_attenuation_protocol(peak_glucose_delta_mg_dl: float, duration_above_140_minutes: float = 0.0) -> Dict[str, Any]:
        interventions = [
            "Perform immediate 15-minute brisk walking or bodyweight soleus pushups to stimulate non-insulin GLUT4 translocation",
            "Drink 1 tablespoon organic apple cider vinegar in 250ml water prior to subsequent meals",
            "Adjust future meal sequence: fiber/vegetables first, proteins/fats second, carbs last"
        ]
        return {
            "acute_spike_delta_mg_dl": peak_glucose_delta_mg_dl,
            "time_above_140_min": duration_above_140_minutes,
            "attenuation_directives": interventions,
            "clinical_goal": "Keep postprandial glucose excursions under 30 mg/dL above pre-meal baseline."
        }
