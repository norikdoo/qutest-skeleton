# tests...

# First test is always after RESET -> cannot use NORESET
test("SKELETON_init() return 0")
command(0, 1)
expect("@timestamp SKELETON SKELETON_init 0")
expect("@timestamp Trg-Done QS_RX_COMMAND")

# Test assertion
test("SKELETON_init() test assertion", NORESET)
command(0, 11)
expect("@timestamp =ASSERT= Mod=SKELETON,Loc=13")

# Test after ASSERT cannot be NORESET
test("SKELETON_init() return param value")
command(0, 6)
expect("@timestamp SKELETON SKELETON_init 6")
expect("@timestamp Trg-Done QS_RX_COMMAND")

# Demo of poke() to modify value of a variable in target memory
test("SKELETON_init() return value of poke()", NORESET)
current_obj(OBJ_AP, "skeleton_value")
poke(0, 4, pack('<L', 30))
command(0, 2)
expect("@timestamp SKELETON SKELETON_init 30")
expect("@timestamp Trg-Done QS_RX_COMMAND")
