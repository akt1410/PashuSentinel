"""
app/services/rag_knowledge.py
─────────────────────────────────────────────────────────────────────────────
Curated veterinary knowledge documents for Pashu Sentinel's RAG system.

Sources / inspiration:
  • ICAR-NIVEDI Disease SOPs & Advisories
  • DAHD Notifiable Disease Guidelines & National Vaccination Protocols
  • NDDB Validated Ethnoveterinary Medicine (EVM) Formulations
  • FAO Animal Production & Health Manual

Each document is a dict with:
  - id:       unique slug
  - title:    human-readable heading
  - category: for metadata filtering
  - language: "en" (Hindi/Marathi translations can be added as separate docs)
  - text:     full document text (plain prose, ~200-600 words)
─────────────────────────────────────────────────────────────────────────────
"""

VET_KNOWLEDGE_DOCS = [
    # ─── FOOT-AND-MOUTH DISEASE ──────────────────────────────────────────────
    {
        "id": "fmd-overview",
        "title": "Foot-and-Mouth Disease (FMD) — Overview & Recognition",
        "category": "disease",
        "language": "en",
        "text": (
            "Foot-and-Mouth Disease (FMD) is a highly contagious viral disease caused by the Aphthovirus "
            "(Picornaviridae family). It affects all cloven-hoofed animals including cattle, buffaloes, sheep, "
            "goats, and pigs. India has serotypes O, A, C, Asia-1 circulating.\n\n"
            "KEY SIGNS: Sudden onset of fever (40-41 degrees C), excessive salivation with ropy drool, painful blisters "
            "(vesicles) on the tongue, gums, dental pad, lips, interdigital spaces, and coronary band of hooves. "
            "Animals may be severely lame and reluctant to stand. Milk production drops sharply in dairy animals. "
            "Mortality in adults is low (1-5%) but rises to 20-50% in calves due to myocarditis.\n\n"
            "TRANSMISSION: Aerosol droplets (up to 60 km in favorable wind), direct contact with infected animals, "
            "contaminated fomites (boots, vehicles, equipment), infected semen, and virus-contaminated milk.\n\n"
            "DIFFERENTIAL DIAGNOSIS: Vesicular Stomatitis, Bovine Viral Diarrhea (BVD), Rinderpest (eradicated but "
            "historically significant), Blue-tongue (non-vesicular). Confirm with OIE-accredited lab.\n\n"
            "IMMEDIATE FIRST-AID (Non-prescription): Isolate affected animals immediately. Wash mouth lesions with "
            "2% alum solution or potassium permanganate (KMnO4) rinse. Apply glycerin with turmeric (antiseptic EVM) "
            "to hoof lesions. Provide soft feed and clean water. Do NOT move animals off-farm.\n\n"
            "BIOSECURITY SOP: Impose movement restriction on the farm immediately. Disinfect entry/exit with 2% "
            "caustic soda (NaOH) footbath. Report to the Block Veterinary Officer (BVO) within 24 hours. "
            "FMD is a List A Notifiable Disease under DAHD. Vaccinate non-affected animals in the herd within the "
            "same 24-hour window using government-supplied FMD vaccine."
        ),
    },
    {
        "id": "fmd-vaccination",
        "title": "FMD National Vaccination Protocol — NADCP Guidelines",
        "category": "vaccination",
        "language": "en",
        "text": (
            "Under India's National Animal Disease Control Programme (NADCP), FMD vaccination is conducted bi-annually "
            "(every 6 months) covering cattle, buffaloes, sheep, goats, and pigs.\n\n"
            "VACCINE: Polyvalent killed oil-adjuvanted vaccine covering serotypes O, A, Asia-1. Supplied free by "
            "state governments through Block Veterinary Centres (BVCs).\n\n"
            "SCHEDULE:\n"
            "Primary: 2 doses, 4 weeks apart, starting from 4 months of age.\n"
            "Booster: Every 6 months (twice yearly, April and October campaigns).\n"
            "Pregnant animals: Vaccinate in the first or third trimester; avoid second trimester.\n\n"
            "COVERAGE TARGETS: 80% or more herd coverage per village required to achieve herd immunity. "
            "Villages with less than 60% coverage are classified as HIGH VULNERABILITY under Pashu Sentinel's risk scoring.\n\n"
            "POST-VACCINATION: Animals may show mild swelling at injection site. Immunity develops in 14-21 days. "
            "Tag all vaccinated animals with official ear tags and record in Bharat Pashudhan portal.\n\n"
            "IMPORTANT: Vaccination does NOT replace movement restrictions during an active outbreak. "
            "Always consult a registered veterinarian (BVO/DVO) for outbreak-specific booster timing."
        ),
    },

    # ─── LUMPY SKIN DISEASE ──────────────────────────────────────────────────
    {
        "id": "lsd-overview",
        "title": "Lumpy Skin Disease (LSD) — Recognition & Response",
        "category": "disease",
        "language": "en",
        "text": (
            "Lumpy Skin Disease (LSD) is a viral disease of cattle and buffaloes caused by the LSD virus (LSDV, "
            "Capripoxvirus). It emerged in India in 2019 and caused a major pan-India outbreak in 2022.\n\n"
            "KEY SIGNS: Fever (40-41 degrees C) for 2-7 days before skin lesions appear. Characteristic firm, round, raised "
            "nodules (2-5 cm diameter) on skin, especially on neck, udder, perineum, limbs, and muzzle. Nodules may "
            "ulcerate and develop necrotic centres. Enlarged lymph nodes, nasal discharge, lacrimation, "
            "reluctance to move, and reduced milk yield. Mortality is low (1-5%) but morbidity is high (10-40%).\n\n"
            "TRANSMISSION: Primarily by blood-feeding insects such as Aedes aegypti mosquitoes, Stomoxys stable flies, "
            "and Culicoides midges (peak during monsoon and post-monsoon seasons). Also by direct contact and "
            "contaminated fomites.\n\n"
            "IMMEDIATE FIRST-AID (Non-prescription): Isolate affected animals from the herd. Apply antiseptic "
            "dressings (povidone-iodine ointment) to ulcerated nodules to prevent secondary bacterial infection. "
            "Use insect-repellent (pyrethroid-based) on the herd. Provide supportive care with vitamins A, D, E.\n\n"
            "BIOSECURITY SOP: Restrict movement of cattle. Safely dispose dead carcasses by deep burial with lime. "
            "Report to BVO immediately. LSD is a notifiable disease. Vaccinate non-affected cattle with "
            "Goat Pox (Uttarkashi strain) or LSD homologous vaccine (Lumpi-ProVacInd by ICAR-NRCE). "
            "Insecticide spraying of the premises is mandatory."
        ),
    },

    # ─── HAEMORRHAGIC SEPTICAEMIA ─────────────────────────────────────────────
    {
        "id": "hs-overview",
        "title": "Haemorrhagic Septicaemia (HS) — Recognition & Emergency Response",
        "category": "disease",
        "language": "en",
        "text": (
            "Haemorrhagic Septicaemia (HS) is a fatal bacterial disease caused by Pasteurella multocida serotype B:2 "
            "and E:2. It is called 'Galgotu' in Hindi. It is one of the most economically devastating cattle and "
            "buffalo diseases in India, with mortality approaching 80-100% if untreated.\n\n"
            "KEY SIGNS: Peracute form means sudden death within 8-24 hours of onset without premonitory signs. "
            "Acute form means high fever (41-42 degrees C), profuse salivation, labored breathing, hot painful swelling in the "
            "throat or brisket region (oedematous swelling), nasal discharge, and death within 12-36 hours.\n\n"
            "RISK FACTORS: Pre-monsoon/monsoon season, high Temperature-Humidity Index (THI greater than 78), transport stress, "
            "overcrowding, and poor nutrition.\n\n"
            "EMERGENCY FIRST-AID: HS progresses extremely rapidly. The ONLY effective intervention is immediate "
            "veterinary treatment with oxytetracycline or sulphonamides (prescription only). "
            "Do NOT delay. Call the BVO IMMEDIATELY and get prescription antibiotics within the first 6 hours. "
            "Ethnoveterinary remedies alone CANNOT save an animal with HS.\n\n"
            "PREVENTION (Non-prescription): Vaccinate all cattle and buffaloes with HS vaccine (alum-precipitated "
            "oil-adjuvanted P. multocida B:2) annually before monsoon (March-April). Ensure adequate shade, clean "
            "water, and reduce overcrowding during high THI periods."
        ),
    },

    # ─── ANTHRAX ─────────────────────────────────────────────────────────────
    {
        "id": "anthrax-overview",
        "title": "Anthrax — Sudden Death & Zoonotic Emergency Protocol",
        "category": "disease",
        "language": "en",
        "text": (
            "Anthrax is caused by Bacillus anthracis spores that survive in soil for decades. It causes peracute "
            "sudden death in cattle, buffalo, sheep, goats, and horses. It is also a serious zoonotic risk as "
            "humans can contract cutaneous anthrax by handling carcasses without protection.\n\n"
            "KEY SIGNS: Peracute means sudden death with bloody discharge from body orifices (nose, mouth, anus, vulva). "
            "No rigor mortis (body remains flaccid). Bloating and rapid decomposition. Sub-acute means high fever, "
            "staggering, dyspnea, sudden collapse.\n\n"
            "CRITICAL ZOONOTIC WARNING: Do NOT perform a post-mortem (necropsy) on any suspected anthrax case. "
            "Cutting the carcass exposes spores to air, massively amplifying environmental contamination. "
            "Do NOT use bare hands to touch the carcass. Use gloves, mask, and protective clothing.\n\n"
            "EMERGENCY PROTOCOL:\n"
            "1. Immediately isolate the area. Do not let other animals graze near the carcass.\n"
            "2. Report to BVO AND the district IDSP (Integrated Disease Surveillance Programme) simultaneously "
            "as Anthrax is a zoonotic emergency under One Health protocol.\n"
            "3. Carcass disposal: Deep burial (more than 6 feet) on-site with abundant quicklime (CaO), OR incineration. "
            "NEVER move the carcass to another location.\n"
            "4. Vaccinate all in-contact animals with Sterne live spore vaccine (annual, mandatory).\n"
            "5. Persons in contact with carcass should immediately report to the nearest PHC for prophylaxis."
        ),
    },

    # ─── BRUCELLOSIS ─────────────────────────────────────────────────────────
    {
        "id": "brucellosis-overview",
        "title": "Brucellosis — Abortion Storm & Zoonotic Risk",
        "category": "disease",
        "language": "en",
        "text": (
            "Brucellosis is caused by Brucella abortus (cattle/buffaloes) and B. melitensis (goats/sheep). "
            "It is the leading infectious cause of abortion in livestock in India and a major zoonotic disease "
            "transmitted to humans through raw milk, meat, and contact with aborted material.\n\n"
            "KEY SIGNS IN ANIMALS: Late-term abortion (last trimester), retained placenta, reduced fertility, "
            "orchitis in bulls. An abortion storm meaning multiple cows aborting within a short period is the "
            "hallmark cluster signal in Pashu Sentinel.\n\n"
            "KEY SIGNS IN HUMANS: Undulant fever (Malta fever) with recurring waves of fever, joint pains, fatigue, "
            "and night sweats. Farmers, milkers, and vets are at high risk.\n\n"
            "ZOONOTIC ALERT: Aborted foetuses, placental material, and vaginal discharge from brucellosis-infected "
            "animals are highly infectious. Wear gloves and protective gear when handling. Boil all milk before "
            "consumption if brucellosis is suspected.\n\n"
            "PREVENTION:\n"
            "Calf-hood vaccination: S19 vaccine (Brucella abortus strain 19) in female calves at 4-8 months. "
            "RB51 vaccine is an alternative.\n"
            "Test-and-Slaughter policy for confirmed reactors (Rose Bengal Plate Test or ELISA).\n"
            "Milk only pasteurized or boiled milk. No raw milk for family consumption.\n\n"
            "Report to BVO and IDSP. Brucellosis is a notifiable zoonotic disease."
        ),
    },

    # ─── PPR ─────────────────────────────────────────────────────────────────
    {
        "id": "ppr-overview",
        "title": "Peste des Petits Ruminants (PPR) — Sheep & Goat Emergency",
        "category": "disease",
        "language": "en",
        "text": (
            "PPR (also called Goat Plague) is a highly contagious viral disease of sheep and goats caused by the "
            "Morbillivirus (same family as measles). India is targeting PPR eradication by 2030 under the NADCP.\n\n"
            "KEY SIGNS: High fever (41-42 degrees C), profuse nasal and eye discharge (mucopurulent), erosive stomatitis "
            "(mouth ulcers), bloody or watery diarrhea, severe respiratory distress, and rapid weight loss. "
            "Mortality rates reach 50-80% in naive flocks. Abortion is common.\n\n"
            "TRANSMISSION: Highly contagious through direct contact, aerosol, contaminated feed and water. Weekly livestock "
            "markets (haats/mandis) are major transmission amplifiers.\n\n"
            "IMMEDIATE FIRST-AID (Non-prescription): Isolate sick animals immediately. Keep them warm and dry. "
            "Provide electrolyte solution for diarrhea (ORS with 1 litre clean water + 1 tsp salt + 1 tsp sugar). "
            "Clean eye discharge with warm saline. Contact BVO for antidiarrheal and supportive treatment.\n\n"
            "VACCINATION: PPR live attenuated vaccine (Sungri-96 or PPR Raksha) is available free of cost from "
            "the state government. Vaccinate all sheep and goats over 3 months of age. Single dose provides 3 years immunity. "
            "Mass vaccination campaigns are run under NADCP. Mandatory reporting to BVO as PPR is a List A notifiable disease."
        ),
    },

    # ─── ETHNOVETERINARY FIRST-AID ────────────────────────────────────────────
    {
        "id": "evm-wound-care",
        "title": "Ethnoveterinary Medicine (EVM) — Wound & Lesion First-Aid",
        "category": "evm",
        "language": "en",
        "text": (
            "NDDB-validated ethnoveterinary medicine (EVM) formulations for wound care and lesion first-aid. "
            "These are safe, non-prescription traditional remedies suitable for use before a veterinarian arrives.\n\n"
            "FOR FOOT LESIONS (FMD hoof blisters, interdigital wounds):\n"
            "Apply paste of neem leaves (Azadirachta indica) crushed with turmeric powder and salt. Strong "
            "antimicrobial and anti-inflammatory properties. Apply twice daily.\n"
            "Alternatively, soak the hoof in a bucket of potassium permanganate solution (KMnO4, pale pink color) "
            "for 10-15 minutes twice daily.\n"
            "Apply a thin layer of pure beeswax or mustard oil on healed lesions to prevent re-infection.\n\n"
            "FOR ORAL ULCERS AND MOUTH LESIONS:\n"
            "Rinse mouth with 2% alum (phitkari) solution using a syringe. It is astringent and promotes healing.\n"
            "Apply honey + turmeric paste on visible ulcers (natural antimicrobial).\n"
            "Provide soft boiled rice or jaggery (gur) water as feed until healing.\n\n"
            "FOR SKIN WOUNDS AND NODULES:\n"
            "Apply povidone-iodine ointment (available OTC) to ulcerated LSD nodules to prevent fly strike.\n"
            "Neem oil diluted 1:3 in coconut oil is an effective wound dressing and fly repellent.\n\n"
            "IMPORTANT: EVM first-aid is supportive only. It does NOT replace veterinary diagnosis or prescription "
            "treatments. Always involve a registered veterinarian (BVO) for any serious disease outbreak."
        ),
    },
    {
        "id": "evm-fever-respiratory",
        "title": "Ethnoveterinary Medicine (EVM) — Fever & Respiratory Support",
        "category": "evm",
        "language": "en",
        "text": (
            "Safe ethnoveterinary supportive care for fever and mild respiratory symptoms in livestock. "
            "These remedies provide relief while awaiting veterinary care. Never use as replacement for diagnosis.\n\n"
            "FOR FEVER (MILD, below 40.5 degrees C):\n"
            "Provide cool, clean water ad libitum. Wet the head and neck with cool water.\n"
            "Provide shade and good ventilation, especially critical in high THI (greater than 78) conditions.\n"
            "Tulsi (Holy Basil, Ocimum sanctum) decoction: boil 50g fresh tulsi leaves in 2 litres water, "
            "cool and drench 500ml twice daily. It acts as an immunostimulant and antipyretic.\n"
            "Giloy (Tinospora cordifolia) decoction: antimicrobial and immunomodulatory. Traditional use for fever in cattle.\n\n"
            "FOR MILD RESPIRATORY SYMPTOMS (Nasal discharge, mild cough):\n"
            "Steam inhalation: Boil water with eucalyptus leaves, position animal's nose over steam for 10-15 minutes.\n"
            "Ginger (adrak) paste mixed with jaggery, 100g each, given as a bolus twice daily. Acts as expectorant.\n"
            "Garlic (lahsun) crushed in mustard oil, drench 50ml. Provides antimicrobial support.\n\n"
            "CRITICAL RULE: If fever exceeds 41 degrees C, animal is gasping or unable to breathe, or throat swelling "
            "is visible, these are signs of Haemorrhagic Septicaemia (HS) or other emergencies requiring IMMEDIATE "
            "prescription antibiotics. Call the BVO immediately. Do NOT rely on EVM alone in such cases."
        ),
    },

    # ─── BIOSECURITY ─────────────────────────────────────────────────────────
    {
        "id": "biosecurity-outbreak",
        "title": "Biosecurity SOP — Farm-Level Outbreak Containment",
        "category": "biosecurity",
        "language": "en",
        "text": (
            "Immediate biosecurity measures to implement when a disease outbreak is suspected or confirmed. "
            "These actions can significantly reduce spread while awaiting official veterinary response.\n\n"
            "STEP 1 - ISOLATE (First 30 minutes):\n"
            "Move all visibly sick animals to a separate pen or shed immediately.\n"
            "Suspend all animal movement out of the farm. No sales, no transport.\n"
            "Block access to any water bodies (ponds, streams) shared with neighboring farms.\n\n"
            "STEP 2 - DISINFECT (First 2 hours):\n"
            "Prepare 2% caustic soda (NaOH) solution for entry/exit footbaths.\n"
            "Spray 5% phenol or 2% formalin in the isolation area and around water troughs.\n"
            "Burn or deep-bury all aborted foetuses, placentas, and heavily contaminated bedding.\n\n"
            "STEP 3 - REPORT (Within 24 hours):\n"
            "Contact the Block Veterinary Officer (BVO). Number available at the nearest BVC or AHD office.\n"
            "Log the case in Pashu Sentinel with full symptom details, number of animals affected, and GPS location.\n"
            "For sudden deaths or abortion storms, also contact the district IDSP (One Health zoonotic protocol).\n\n"
            "STEP 4 - PROTECT PERSONNEL:\n"
            "Anyone handling sick animals must wear rubber gloves, boots, and mask, especially for suspected "
            "Anthrax, Brucellosis, or Rabies cases.\n"
            "Wash hands thoroughly with soap after all animal contact.\n"
            "Do NOT consume raw milk from affected animals during an outbreak."
        ),
    },

    # ─── BVD ─────────────────────────────────────────────────────────────────
    {
        "id": "bvd-overview",
        "title": "Bovine Viral Diarrhoea (BVD) & Enteric Diseases — Recognition",
        "category": "disease",
        "language": "en",
        "text": (
            "Enteric (gut) diseases causing diarrhoea are among the most common and economically significant livestock "
            "conditions in India. Key causes include BVD virus, Salmonella, Rotavirus, Coronavirus, and Johne's Disease.\n\n"
            "KEY SIGNS - CALL TO ACTION LEVELS:\n"
            "Mild (watery diarrhoea, alert animal): ORS + EVM care, monitor closely.\n"
            "Moderate (bloody diarrhoea, weakness, sunken eyes): Contact BVO urgently.\n"
            "Severe (unable to stand, severe dehydration, cold extremities): Veterinary emergency. Call BVO now.\n\n"
            "IMMEDIATE FIRST-AID (Non-prescription):\n"
            "ORS: 1 litre clean boiled water + 1 tsp table salt + 1 tsp sugar + 1 tsp potassium chloride (optional). "
            "Drench 1-2 litres every 4-6 hours for adults; 250-500ml for calves.\n"
            "Kaolin-pectin suspension (OTC): Reduces gut inflammation and watery diarrhoea.\n"
            "Withhold coarse feed temporarily; provide dry hay and clean water.\n"
            "Isolate to prevent spread. Enteric diseases are highly contagious via the fecal-oral route.\n\n"
            "FOR NEONATAL CALF DIARRHOEA (SCOURS, most common killer in calves less than 2 weeks of age):\n"
            "Aggressive ORS therapy is the cornerstone of treatment. Calves can die within 24-48 hours of "
            "dehydration. Ensure the calf is warm, dry, and receiving electrolytes.\n"
            "Contact BVO immediately if the calf cannot stand or has severe sunken eyes."
        ),
    },

    # ─── RABIES ──────────────────────────────────────────────────────────────
    {
        "id": "rabies-overview",
        "title": "Rabies in Livestock — Zoonotic Emergency Protocol",
        "category": "disease",
        "language": "en",
        "text": (
            "Rabies is a fatal viral zoonotic disease caused by the Rabies lyssavirus. In livestock, cattle and "
            "buffaloes are most affected, typically through dog bites. ALL human exposures are medical emergencies.\n\n"
            "KEY SIGNS IN ANIMALS:\n"
            "Furious Form: Restlessness, aggression, bellowing, self-mutilation, attacking objects and people.\n"
            "Dumb or Paralytic Form (more common in cattle): Progressive paralysis, drooling, inability to swallow, "
            "dropped jaw, bloat. Often mistaken for a foreign body in throat.\n\n"
            "CRITICAL ZOONOTIC EMERGENCY - IMMEDIATE ACTIONS:\n"
            "1. Do NOT approach or handle the animal without protection. Keep ALL people and other animals away.\n"
            "2. If any person has been bitten or had contact with the animal's saliva on broken skin:\n"
            "Wash wound immediately with soap and water for 15 minutes.\n"
            "Go to the nearest hospital PHC or CHC IMMEDIATELY for Post-Exposure Prophylaxis (PEP, anti-rabies "
            "vaccination). PEP MUST start within 24-72 hours. Delay is life-threatening.\n"
            "3. Report to BVO and district IDSP simultaneously.\n"
            "4. Euthanase the animal humanely and submit brain tissue to state veterinary lab for confirmation.\n"
            "5. Vaccinate all dogs on the farm and in the surrounding village against rabies.\n\n"
            "PREVENTION: Annual anti-rabies vaccination of all dogs is the single most effective prevention measure. "
            "Vaccinate cattle in endemic areas with ERA live attenuated rabies vaccine."
        ),
    },

    # ─── WHEN TO CALL THE VET ────────────────────────────────────────────────
    {
        "id": "emergency-escalation",
        "title": "When to Call the Veterinarian — Emergency Escalation Guide",
        "category": "guidance",
        "language": "en",
        "text": (
            "Pashu Sentinel's RAG system provides first-aid guidance and biosecurity SOPs. However, certain symptoms "
            "ALWAYS require immediate professional veterinary care. Use this guide to decide when to escalate.\n\n"
            "CALL THE VETERINARIAN IMMEDIATELY (same day) if you see:\n"
            "Sudden death of one or more animals with no prior symptoms.\n"
            "Bloody discharge from any body orifice (mouth, nose, anus).\n"
            "Visible throat or brisket swelling + high fever (above 41 degrees C).\n"
            "Seizures, convulsions, or inability to walk or stand.\n"
            "Multiple abortions in the herd within a short period.\n"
            "Suspected rabies (aggression, paralysis, drooling).\n"
            "Suspected anthrax (sudden death + bloody discharge + no rigor mortis).\n"
            "Any animal that appears to be in severe pain or distress.\n\n"
            "CALL THE VETERINARIAN URGENTLY (within 24 hours) if you see:\n"
            "Blisters or vesicles on mouth, tongue, or feet (suspect FMD).\n"
            "Large nodular skin lesions appearing rapidly (suspect LSD).\n"
            "Severe diarrhoea not responding to ORS within 12 hours.\n"
            "More than 10% of the herd showing the same symptoms simultaneously.\n"
            "Milk production drop of more than 50% across the herd within 24-48 hours.\n\n"
            "HOW TO REACH THE BVO:\n"
            "Block Veterinary Centre (BVC): Visit in person or call the block office.\n"
            "Pashu Kisan Credit Card holders: Emergency helpline 1962 (DAHD Animal Helpline).\n"
            "Log the case in Pashu Sentinel. The system will automatically alert the nearest VET."
        ),
    },

    # ─── VETERINARY CLINICAL DECISION SUPPORT (CDSS) PROTOCOLS ─────────────────
    {
        "id": "vet-differential-vesicular",
        "title": "Veterinary Clinical Protocol — Differential Diagnosis Matrix for Vesicular & Podal Syndromes",
        "category": "clinical_protocol",
        "language": "en",
        "text": (
            "CLINICAL DECISION SUPPORT FOR REGISTERED VETERINARIANS (BVO / VO / DVO):\n"
            "Differential diagnosis and clinical distinction for cloven-hoofed animals presenting with vesicular, "
            "erosive, or ulcerative lesions on oral mucosa, tongue, dental pad, coronary band, or interdigital cleft.\n\n"
            "DIFFERENTIAL MATRIX:\n"
            "1. Foot-and-Mouth Disease (FMD — Aphthovirus, Picornaviridae):\n"
            "   - Affected species: Cattle, buffalo, sheep, goat, pigs (NOT horses/equines).\n"
            "   - Pathognomonic signs: Sudden high pyrexia (40-41.5°C), profuse ropy salivation, painful vesicles that rupture "
            "within 24-48 hours leaving raw, red erosions with ragged edges on tongue and dental pad. Severe podal lesions, "
            "interdigital ulceration, coronary band separation, severe lameness. Tiger heart (myocarditis) in calves.\n"
            "   - Contagion index: Extremely high (R0 > 20 in close housing); rapid aerosol transmission up to 60 km.\n\n"
            "2. Vesicular Stomatitis (VS — Vesiculovirus, Rhabdoviridae):\n"
            "   - Critical distinction: AFFECTS HORSES AND EQUINES as well as cattle and pigs. If equines on the property exhibit "
            "vesicular stomatitis, strongly suspect VS over FMD.\n"
            "   - Lesions clinically indistinguishable from FMD in cattle; laboratory confirmation mandatory.\n\n"
            "3. Bovine Viral Diarrhea / Mucosal Disease (BVDV — Pestivirus, Flaviviridae):\n"
            "   - Key signs: Punched-out linear erosions throughout the alimentary tract, oral erosions without distinct intact "
            "vesicles, accompanied by profuse watery foul-smelling diarrhea, leukopenia, coronary band necrosis, but rarely "
            "large ruptured vesicles on the tongue.\n\n"
            "4. Bluetongue (Orbivirus, Reoviridae):\n"
            "   - Affected species: Primarily sheep; cattle serve as reservoir (usually subclinical or mild).\n"
            "   - Distinguishing signs: Hyperemia of muzzle ('strawberry mouth'), cyanotic swollen tongue, submandibular edema, "
            "coronitis (red band above hoof), vector-borne (Culicoides midges).\n\n"
            "5. Malignant Catarrhal Fever (MCF — Alcelaphine/Ovine Herpesvirus 2):\n"
            "   - Distinguishing signs: Bilateral corneal opacity (centripetal keratitis), profuse mucopurulent oculonasal discharge, "
            "crusted muzzle, generalized lymphadenopathy, CNS signs. Low morbidity (sporadic), near 100% case fatality.\n\n"
            "LABORATORY CONFIRMATION PROTOCOL:\n"
            "Gold standard: Epithelial tissue flaps (minimum 1g) or vesicular fluid submitted to ICAR-DFMD / ICAR-NIHSAD Bhopal. "
            "Perform real-time RT-PCR (3D/5'-UTR genes) and antigen detection ELISA for serotyping (O, A, Asia-1)."
        ),
    },
    {
        "id": "vet-differential-respiratory",
        "title": "Veterinary Clinical Protocol — Acute Respiratory Syndrome Differentials (Bovine & Small Ruminants)",
        "category": "clinical_protocol",
        "language": "en",
        "text": (
            "CLINICAL DECISION SUPPORT FOR VETERINARIANS — ACUTE RESPIRATORY DISTRESS & EDEMA:\n"
            "Evaluation of acute dyspnea, tracheal rattling, frothy/mucopurulent discharge, and sudden systemic collapse.\n\n"
            "DIFFERENTIAL MATRIX:\n"
            "1. Haemorrhagic Septicaemia (HS — Pasteurella multocida B:2):\n"
            "   - Pathognomonic markers: Acute to peracute onset, severe pyrexia (41-42°C), profuse salivation, hot, painful, "
            "doughy inflammatory swelling of the throat, submandibular region, and brisket. Severe inspiratory dyspnea with "
            "gurgling or stertorous breathing. Progresses to death within 8-24 hours due to endotoxic shock and asphyxiation.\n"
            "   - Cytology: Bipolar staining bacilli on blood smear stained with Leishman or methylene blue.\n\n"
            "2. Contagious Bovine Pleuropneumonia (CBPP — Mycoplasma mycoides subsp. mycoides):\n"
            "   - Clinical markers: Chronic or subacute coughing, abduction of elbows, arched back, extended head, unilateral "
            "or bilateral dullness on thoracic percussion. Marbled lung appearance with interlobular septal distension on post-mortem.\n\n"
            "3. Peste des Petits Ruminants (PPR — Morbillivirus, Small Ruminants):\n"
            "   - Key presentation in sheep/goats: Pyrexia, serous to mucopurulent oculonasal discharge crusting the nares, "
            "necrotic stomatitis with halitosis, progressing within 2-3 days to severe watery/bloody diarrhea and broncho-pneumonia.\n\n"
            "4. Bovine Respiratory Disease Complex (BRDC / Shipping Fever):\n"
            "   - Multifactorial: Viral precursors (BRSV, IBR, PI-3) complicated by secondary Mannheimia haemolytica or P. multocida. "
            "Triggered by transport stress, exhaustion, sudden weather transitions.\n\n"
            "STATUTORY VETERINARY ACTION:\n"
            "For suspected HS, immediate emergency antimicrobial intervention within 6 hours (Oxytetracycline 10 mg/kg IV/IM or "
            "Sulfamethazine 33.3% 100 mg/kg IV). Deep carcass burial with lime. Mandatory reporting to DVO command center."
        ),
    },
    {
        "id": "vet-lab-sampling-sop",
        "title": "Veterinary Laboratory Specimen Collection, Cold-Chain & Referral Routing SOP",
        "category": "lab_sop",
        "language": "en",
        "text": (
            "OFFICIAL FIELD VETERINARY LABORATORY REFERRAL AND SAMPLE TRANSPORT PROTOCOL (ICAR / DAHD / WOAH):\n\n"
            "SAMPLE COLLECTION GUIDELINES PER SUSPECTED CONDITION:\n"
            "1. Vesicular Syndromes (FMD / VS / LSD):\n"
            "   - Epithelial flaps: Minimum 1-2 grams of unruptured or freshly ruptured vesicle wall (tongue or foot).\n"
            "   - Preservative: 50% phosphate-buffered glycerol (PBS-glycerol, pH 7.2-7.6). Do NOT use formalin.\n"
            "   - Vesicular fluid: Aspirate 0.5-2 ml with a sterile 21G syringe and transfer to sterile cryovial.\n"
            "   - Scabs / Skin nodules (LSD): 4 mm punch biopsy or deep crust scrapings in sterile dry vial or PBS.\n\n"
            "2. Septicemic / Sudden Death (HS / Anthrax / Blackleg):\n"
            "   - Suspected Anthrax: NEVER OPEN THE CARCASS. Make a blood smear from an ear vein or tip of tail. Dry and fix with "
            "methanol. Seal in airtight slide box. Swab exudate using sterile cotton swab.\n"
            "   - HS: Aspirate edematous fluid from brisket or collect peripheral blood during the febrile pre-lethal peak into EDTA tubes.\n\n"
            "3. Abortion Storms (Brucellosis):\n"
            "   - Aborted fetal stomach contents (aspirated with sterile syringe), cotyledons/placental tissue, maternal paired serum.\n"
            "   - Extreme zoonotic hazard: Full PPE (N95 mask, double nitrile gloves, eye protection) mandatory.\n\n"
            "COLD-CHAIN & TRANSIT SPECIFICATIONS:\n"
            "   - Transit < 24-48 hours: Maintain strictly at 2°C to 4°C using conditioned frozen gel ice packs in insulated thermo-cool containers.\n"
            "   - Transit > 48 hours or virus isolation: Dry ice (-70°C) or liquid nitrogen shipper.\n"
            "   - Packaging standard: IATA 650 Triple Packaging (Primary leakproof receptacle, secondary leakproof packaging with absorbent material, "
            "rigid outer container with biohazard labeling).\n\n"
            "REFERRAL LABORATORY ROUTING:\n"
            "   - National Reference Labs: ICAR-NIHSAD Bhopal (High Security Animal Disease), ICAR-DFMD Mukteshwar / Bengaluru (FMD), "
            "ICAR-IVRI CADRAD Bareilly (General pathology & toxicology).\n"
            "   - State / Regional Labs: Regional Disease Diagnostic Laboratory (RDDL Pune for Western Zone, Maharashtra)."
        ),
    },
    {
        "id": "vet-therapeutics-stewardship",
        "title": "Veterinary Clinical Therapeutics & Antimicrobial Stewardship Guidelines (DAHD/ICAR)",
        "category": "clinical_protocol",
        "language": "en",
        "text": (
            "CLINICAL THERAPEUTICS & ANTIMICROBIAL STEWARDSHIP MANUAL FOR BLOCK VETERINARY SURGEONS:\n\n"
            "1. SUPPORTIVE THERAPY IN VIRAL EPIZOOTICS (FMD / LSD / PPR):\n"
            "   - Fluid & Electrolyte Resuscitation: Crystalloid infusion (Normal Saline 0.9% or Ringer's Lactate) for anorexic or "
            "dehydrated animals. Maintenance volume: 50-60 ml/kg/day in adults; 80-100 ml/kg/day in recumbent calves.\n"
            "   - Analgesia & Antipyresis: Flunixin meglumine 1.1-2.2 mg/kg IV/IM once daily (maximum 3 days) or Meloxicam 0.5 mg/kg IV/IM. "
            "Provides potent anti-inflammatory relief, reduces oral pain, and restores early feed intake.\n"
            "   - Topical Antiseptic Dressings: Oral cavity rinse with 2% sodium bicarbonate or 0.1% potassium permanganate; "
            "foot baths with 4% sodium carbonate. Zinc oxide or boric acid ointment on healing lesions.\n\n"
            "2. ANTIMICROBIAL STEWARDSHIP (AMS) RULES (GOVERNMENT OF INDIA DAHD GUIDELINES):\n"
            "   - NEVER administer antibiotics for uncomplicated viral diseases as prophylaxis. Reserve antimicrobials only for secondary "
            "bacterial infections (fever persisting > 72 hours, purulent discharge, deep tissue necrosis).\n"
            "   - First-Line Access Class: Procaine Penicillin (20,000 IU/kg IM) + Streptomycin, or Amoxicillin (10 mg/kg IM), or "
            "Oxytetracycline (10 mg/kg IM). Narrow-spectrum antimicrobials must be prioritized.\n"
            "   - Reserve Class (Cephalosporins 3rd/4th gen, Fluoroquinolones): STRICTLY RESTRICTED. Indicated only in life-threatening "
            "sepsis where first-line agents fail or guided by antimicrobial susceptibility testing (AST).\n\n"
            "3. STATUTORY WITHDRAWAL PERIODS (FOOD SAFETY & RESIDUE CONTROL):\n"
            "   - Milk withdrawal: Minimum 72-96 hours post-last antibiotic dose; discard or pasteurize non-commercial milk.\n"
            "   - Meat withdrawal: 14 to 28 days depending on formulated excipient.\n"
            "   - Educate livestock owners on the economic and public health hazards of antibiotic residues in milk supply chains."
        ),
    },
    {
        "id": "vet-containment-protocol",
        "title": "Epizootic Ring Containment, Buffer Zones & Movement Geofencing SOP",
        "category": "containment_sop",
        "language": "en",
        "text": (
            "OPERATIONAL CONTAINMENT & GEOFENCING PROTOCOL FOR DISTRICT VETERINARY OFFICERS (DVO) & SURVEILLANCE TEAMS:\n\n"
            "PASHU SENTINEL THREE-TIER CONCENTRIC GEOSPATIAL ZONING:\n"
            "1. Infected Zone (0 to 1 km Radius around Outbreak Epicenter):\n"
            "   - Complete quarantine: Strict prohibition of cloven-hoofed animal ingress and egress.\n"
            "   - Total restriction of vehicle movement into livestock premises without tire disinfection (2% sodium hydroxide / 4% washing soda).\n"
            "   - In situ treatment of affected animals; zero movement of fodder, manure, milk, or carcasses outside the zone.\n"
            "   - Disinfection checkpoints at all village arterial exit points.\n\n"
            "2. Protection Zone (1 to 3 km Radius Buffer):\n"
            "   - Immediate Ring Vaccination: Mobilize Mobile Veterinary Units (MVUs) to vaccinate 100% of susceptible livestock "
            "within 48 to 72 hours using the designated government homologue vaccine (NADCP).\n"
            "   - Daily syndromic active surveillance by Para-vets / Pashu Sakhis with digital outbox reporting via Pashu Sentinel.\n"
            "   - Immediate prohibition of Artificial Insemination (AI) services and breeding bull transit.\n\n"
            "3. Surveillance Zone (3 to 10 km Radius Outer Buffer):\n"
            "   - Immediate closure of all weekly livestock markets (animal haats/mandis), fairs, and trading hubs.\n"
            "   - Automated geofenced broadcast alerts dispatched to all registered dairy farmers and para-vets.\n"
            "   - Active monitoring of milk collection centers (BMC chilling centers) for sudden volume drops indicating subclinical spread.\n\n"
            "ESCALATION TIMELINE TO DISTRICT DISASTER MANAGEMENT AUTHORITY (DDMA):\n"
            "   - Hour 0: Field report verified by BVO on Pashu Sentinel dashboard.\n"
            "   - Hour 2: Automated ST-Buffer rings generated (3 km / 10 km PostGIS polygons).\n"
            "   - Hour 4: Formal outbreak alert transmitted to DVO and District Collector.\n"
            "   - Hour 6: Section 144 / Livestock Contagious Diseases Act notification drafted for interstate highway checkpoints."
        ),
    },
]

