.NAME:New workflow
.GROUP:Test group
.ALGORITHM:beam:aatsr.sst
.PARAMETERS:{"nadirCoefficientsFile": 0, "dualCoefficientsFile": 0, "nadirMaskExpression": "!cloud_flags_nadir.LAND and !cloud_flags_nadir.CLOUDY and !cloud_flags_nadir.SUN_GLINT", "invalidSstValue": -999, "dual": true, "dualMaskExpression": "!cloud_flags_nadir.LAND and !cloud_flags_nadir.CLOUDY and !cloud_flags_nadir.SUN_GLINT and !cloud_flags_fward.LAND and !cloud_flags_fward.CLOUDY and !cloud_flags_fward.SUN_GLINT", "nadir": true}
.MODE:Normal
.INSTRUCTIONS:
!INSTRUCTIONS
