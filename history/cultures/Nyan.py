from pathlib import Path
path = Path.cwd()

files = [e for e in path.iterdir() if e.is_file()]
print(files)


for file in files:
	with open(file, 'a') as f:
		f.write("""

1100.1.1 = {
	#50 years after High Medieval, Early Medieval Free	
	join_era = culture_era_high_medieval
	#
	discover_innovation = innovation_armilary_sphere
	discover_innovation = innovation_baliffs
	discover_innovation = innovation_chronicle_writing
	discover_innovation = innovation_currency_02
	discover_innovation = innovation_development_02
	discover_innovation = innovation_hereditary_rule
	discover_innovation = innovation_manorialism
	discover_innovation = innovation_royal_prerogative
	#
	discover_innovation = innovation_battlements
	discover_innovation = innovation_burhs
	discover_innovation = innovation_arched_saddle
	discover_innovation = innovation_house_soldiers
	discover_innovation = innovation_horseshoes
	discover_innovation = innovation_mangonel
}

1250.1.1 = {
	#50 years after late Medieval, High Medieval Free	
	join_era = culture_era_late_medieval
	#
	discover_innovation = innovation_currency_03
	discover_innovation = innovation_divine_right
	discover_innovation = innovation_guilds
	discover_innovation = innovation_heraldry
	discover_innovation = innovation_land_grants
	discover_innovation = innovation_scutage
	discover_innovation = innovation_development_03
	discover_innovation = innovation_windmills
	#
	discover_innovation = innovation_advanced_bowmaking
	discover_innovation = innovation_castle_baileys
	discover_innovation = innovation_hoardings
	discover_innovation = innovation_knighthood
	discover_innovation = innovation_men_at_arms
	discover_innovation = innovation_trebuchet
}

1400.1.1. = {
	#50 years after count Flandy's 1350 innovation tree, Late Medieval free
	#
	discover_innovation = innovation_court_officials
	discover_innovation = innovation_cranes
	discover_innovation = innovation_ermine_cloaks
	discover_innovation = innovation_noblesse_oblige
	discover_innovation = innovation_primogeniture
	discover_innovation = innovation_currency_04
	discover_innovation = innovation_development_04
	discover_innovation = innovation_rightful_ownership
	#
	discover_innovation = innovation_bombard
	discover_innovation = innovation_machicolations
	discover_innovation = innovation_plate_armor
	discover_innovation = innovation_royal_armory
	discover_innovation = innovation_sappers
	discover_innovation = innovation_trebuchet
} """)



			