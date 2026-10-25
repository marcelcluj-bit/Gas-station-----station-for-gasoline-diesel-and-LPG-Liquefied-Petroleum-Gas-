import json
from datetime import datetime

class HighwayEnergyHubBuilder:
    """
    Core framework for building and operating a modern, modular Highway Energy Station.
    Focuses on civil engineering milestones, EV grid management, retail revenue streams,
    and Web3 RWA asset tokenization.
    """
    def __init__(self, location_id: str, total_area_sqm: float = 15000.0):
        self.location_id = location_id
        self.total_area_sqm = total_area_sqm
        self.construction_status = "PLANNING_AND_PERMITTING"
        self.fuel_capacity_liters = 150000.0  # Compartmentalized double-walled storage
        self.ev_charging_capacity_kw = 1200.0  # Ultra-fast EV charging grid capacity
        self.active_ev_charging_ports = 8
        self.solar_pv_installed_kwp = 250.0

    def advance_construction_stage(self, stage_name: str):
        """
        Tracks civil engineering progress: Terasaments, Heavy Pavement, Underground Tanks, Canopy, Store.
        """
        valid_stages = [
            "PERMITTING_AND_CNAIR_APPROVAL",
            "EARTHWORKS_AND_HEAVY_CONCRETE_PLATFORM",
            "UNDERGROUND_EQUIPMENT_INSTALLATION",
            "CANOPY_DISPENSERS_AND_EV_HUB_SETUP",
            "STORE_AND_FOOD_COURT_FINISHING",
            "COMMISSIONING_AND_LAUNCH"
        ]
        
        if stage_name in valid_stages:
            self.construction_status = stage_name
            return {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "location_id": self.location_id,
                "current_construction_stage": self.construction_status,
                "status": "STAGE_UPDATED_SUCCESSFULLY"
            }
        return {"status": "INVALID_STAGE"}

    def allocate_ev_charger_power(self, requested_kw: float):
        """
        Dynamic load balancing for ultra-fast EV chargers (150kW - 350kW).
        Combines Grid Power + On-site Solar PV Generation.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        available_power_kw = self.ev_charging_capacity_kw + self.solar_pv_installed_kwp
        
        allocated_kw = min(requested_kw, available_power_kw)
        
        return {
            "timestamp": timestamp,
            "location_id": self.location_id,
            "requested_power_kw": requested_kw,
            "allocated_power_kw": allocated_kw,
            "solar_contribution_kwp": self.solar_pv_installed_kwp,
            "grid_status": "STABLE_LOAD_BALANCED"
        }

    def simulate_rwa_asset_yield(self, monthly_retail_and_ev_revenue_usd: float, total_tokens: int = 1_000_000):
        """
        Calculates Web3 RWA revenue share based on non-fuel retail margins, food court sales, and EV charging fees.
        """
        # Allocates a clean 15% net yield directly from high-margin retail/EV operations
        dividend_pool_usd = monthly_retail_and_ev_revenue_usd * 0.15
        yield_per_token = dividend_pool_usd / total_tokens
        
        return {
            "monthly_retail_and_ev_revenue_usd": monthly_retail_and_ev_revenue_usd,
            "distributed_dividend_pool_usd": round(dividend_pool_usd, 2),
            "total_rwa_tokens": total_tokens,
            "yield_per_token_usd": round(yield_per_token, 6),
            "smart_contract_status": "READY_FOR_ONCHAIN_DISBURSEMENT"
        }

# Execution Entry Point
if __name__ == "__main__":
    hub_builder = HighwayEnergyHubBuilder(location_id="HUB-HIGHWAY-A1-KM120")
    
    print("=== 1. STADIU CONSTRUCȚIE ȘI INFRASTRUCTURĂ CIVILĂ ===")
    stage_1 = hub_builder.advance_construction_stage("EARTHWORKS_AND_HEAVY_CONCRETE_PLATFORM")
    print(json.dumps(stage_1, indent=2))
    
    print("\n=== 2. BALANSAREA DINAMICĂ A PUTEREI PENTRU STATII EV ULTRA-RAPIDE ===")
    ev_power = hub_builder.allocate_ev_charger_power(requested_kw=350.0)
    print(json.dumps(ev_power, indent=2))
    
    print("\n=== 3. TOKENIZARE RWA ȘI DISTRIBUȚIE RANDAMENT ON-CHAIN ===")
    yield_dist = hub_builder.simulate_rwa_asset_yield(monthly_retail_and_ev_revenue_usd=180000.0)
    print(json.dumps(yield_dist, indent=2))
