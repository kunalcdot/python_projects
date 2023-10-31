RegIntfSel_add = "00"

# pol_array = [id,reg_add,bit_no,return_true,return_false]
pol_array = [
["label_card_name","0x1",0,"NA","NA"],	# to display data.. 
["label_epld_ver","0x0",0,"NA","NA"],
["zl_status","0x0",4,"Locked","Not Locked"],

["rim_ps_status","0x90",2,"Not Present","Present"],
["tp_rst_status","0x90",4,"Out of Reset","In Reset"],
["mcp_rst_status","0x90",5,"Out of Reset","In Reset"],
["master_dis_status","0x91",3,"Ports Enabled","Ports Disabled"],

["srr_phy_rst_status","0x84",5,"Out of Reset","In Reset"],
["sfp0_txflt","0x92",2,"Fault","No Fault"],
["sfp0_rxlos","0x92",1,"LOS","No LOS"],
["sfp0_modabs","0x92",0,"Absent","Present"],
["sfp1_txflt","0x92",6,"Fault","No Fault"],
["sfp1_rxlos","0x92",5,"LOS","No LOS"],
["sfp1_modabs","0x92",4,"Absent","Present"],
["coma_mode_status","0x89",7,"High","Low"]


]