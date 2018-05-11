header = [
  "runNumber", "eventNumber", "weight",
  "j1_px", "j1_py", "j1_pz", "j1_E", "j1_m", "j1_mv2c10",
  "j2_px", "j2_py", "j2_pz", "j2_E", "j2_m", "j2_mv2c10",
  "j3_px", "j3_py", "j3_pz", "j3_E", "j3_m", "j3_mv2c10",
  "j4_px", "j4_py", "j4_pz", "j4_E", "j4_m", "j4_mv2c10",
  "j5_px", "j5_py", "j5_pz", "j5_E", "j5_m", "j5_mv2c10",
  "j6_px", "j6_py", "j6_pz", "j6_E", "j6_m", "j6_mv2c10",
  "j7_px", "j7_py", "j7_pz", "j7_E", "j7_m", "j7_mv2c10",
  "t_px",  "t_py",  "t_pz",  "t_E",  "t_m", 
  "tb_px", "tb_py", "tb_pz", "tb_E", "tb_m", 
]

input_features = [
  "j1_px", "j1_py", "j1_pz", "j1_E", "j1_m", "j1_mv2c10",
  "j2_px", "j2_py", "j2_pz", "j2_E", "j2_m", "j2_mv2c10",
  "j3_px", "j3_py", "j3_pz", "j3_E", "j3_m", "j3_mv2c10",
  "j4_px", "j4_py", "j4_pz", "j4_E", "j4_m", "j4_mv2c10",
  "j5_px", "j5_py", "j5_pz", "j5_E", "j5_m", "j5_mv2c10",
  "j6_px", "j6_py", "j6_pz", "j6_E", "j6_m", "j6_mv2c10",
  "j7_px", "j7_py", "j7_pz", "j7_E", "j7_m", "j7_mv2c10",
]

target_features = [
  "t_px",  "t_py",  "t_pz",  "t_E",  "t_m",
  "tb_px", "tb_py", "tb_pz", "tb_E", "tb_m",
]

n_jets_per_event   = 7
n_features_per_jet = 6 # (px, py, pz, E, M, bw )
n_features_per_top = 5 # (px, py, pz, E, M )


