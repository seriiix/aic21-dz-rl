from collections import OrderedDict
import torch

NN = OrderedDict() 

from V_conv1_weight import V_CONV1_WEIGHT
NN["CONV1.WEIGHT".lower()] = torch.Tensor(V_CONV1_WEIGHT)
from V_conv1_bias import V_CONV1_BIAS
NN["CONV1.BIAS".lower()] = torch.Tensor(V_CONV1_BIAS)
from V_conv2_weight import V_CONV2_WEIGHT
NN["CONV2.WEIGHT".lower()] = torch.Tensor(V_CONV2_WEIGHT)
from V_conv2_bias import V_CONV2_BIAS
NN["CONV2.BIAS".lower()] = torch.Tensor(V_CONV2_BIAS)
from V_conv3_weight import V_CONV3_WEIGHT
NN["CONV3.WEIGHT".lower()] = torch.Tensor(V_CONV3_WEIGHT)
from V_conv3_bias import V_CONV3_BIAS
NN["CONV3.BIAS".lower()] = torch.Tensor(V_CONV3_BIAS)

V_FC1_WEIGHT = []
from V_fc1_weight_0 import V_FC1_WEIGHT_0
V_FC1_WEIGHT.append(V_FC1_WEIGHT_0)
from V_fc1_weight_1 import V_FC1_WEIGHT_1
V_FC1_WEIGHT.append(V_FC1_WEIGHT_1)
from V_fc1_weight_2 import V_FC1_WEIGHT_2
V_FC1_WEIGHT.append(V_FC1_WEIGHT_2)
from V_fc1_weight_3 import V_FC1_WEIGHT_3
V_FC1_WEIGHT.append(V_FC1_WEIGHT_3)
from V_fc1_weight_4 import V_FC1_WEIGHT_4
V_FC1_WEIGHT.append(V_FC1_WEIGHT_4)
from V_fc1_weight_5 import V_FC1_WEIGHT_5
V_FC1_WEIGHT.append(V_FC1_WEIGHT_5)
from V_fc1_weight_6 import V_FC1_WEIGHT_6
V_FC1_WEIGHT.append(V_FC1_WEIGHT_6)
from V_fc1_weight_7 import V_FC1_WEIGHT_7
V_FC1_WEIGHT.append(V_FC1_WEIGHT_7)
from V_fc1_weight_8 import V_FC1_WEIGHT_8
V_FC1_WEIGHT.append(V_FC1_WEIGHT_8)
from V_fc1_weight_9 import V_FC1_WEIGHT_9
V_FC1_WEIGHT.append(V_FC1_WEIGHT_9)
from V_fc1_weight_10 import V_FC1_WEIGHT_10
V_FC1_WEIGHT.append(V_FC1_WEIGHT_10)
from V_fc1_weight_11 import V_FC1_WEIGHT_11
V_FC1_WEIGHT.append(V_FC1_WEIGHT_11)
from V_fc1_weight_12 import V_FC1_WEIGHT_12
V_FC1_WEIGHT.append(V_FC1_WEIGHT_12)
from V_fc1_weight_13 import V_FC1_WEIGHT_13
V_FC1_WEIGHT.append(V_FC1_WEIGHT_13)
from V_fc1_weight_14 import V_FC1_WEIGHT_14
V_FC1_WEIGHT.append(V_FC1_WEIGHT_14)
from V_fc1_weight_15 import V_FC1_WEIGHT_15
V_FC1_WEIGHT.append(V_FC1_WEIGHT_15)
from V_fc1_weight_16 import V_FC1_WEIGHT_16
V_FC1_WEIGHT.append(V_FC1_WEIGHT_16)
from V_fc1_weight_17 import V_FC1_WEIGHT_17
V_FC1_WEIGHT.append(V_FC1_WEIGHT_17)
from V_fc1_weight_18 import V_FC1_WEIGHT_18
V_FC1_WEIGHT.append(V_FC1_WEIGHT_18)
from V_fc1_weight_19 import V_FC1_WEIGHT_19
V_FC1_WEIGHT.append(V_FC1_WEIGHT_19)
from V_fc1_weight_20 import V_FC1_WEIGHT_20
V_FC1_WEIGHT.append(V_FC1_WEIGHT_20)
from V_fc1_weight_21 import V_FC1_WEIGHT_21
V_FC1_WEIGHT.append(V_FC1_WEIGHT_21)
from V_fc1_weight_22 import V_FC1_WEIGHT_22
V_FC1_WEIGHT.append(V_FC1_WEIGHT_22)
from V_fc1_weight_23 import V_FC1_WEIGHT_23
V_FC1_WEIGHT.append(V_FC1_WEIGHT_23)
from V_fc1_weight_24 import V_FC1_WEIGHT_24
V_FC1_WEIGHT.append(V_FC1_WEIGHT_24)
from V_fc1_weight_25 import V_FC1_WEIGHT_25
V_FC1_WEIGHT.append(V_FC1_WEIGHT_25)
from V_fc1_weight_26 import V_FC1_WEIGHT_26
V_FC1_WEIGHT.append(V_FC1_WEIGHT_26)
from V_fc1_weight_27 import V_FC1_WEIGHT_27
V_FC1_WEIGHT.append(V_FC1_WEIGHT_27)
from V_fc1_weight_28 import V_FC1_WEIGHT_28
V_FC1_WEIGHT.append(V_FC1_WEIGHT_28)
from V_fc1_weight_29 import V_FC1_WEIGHT_29
V_FC1_WEIGHT.append(V_FC1_WEIGHT_29)
from V_fc1_weight_30 import V_FC1_WEIGHT_30
V_FC1_WEIGHT.append(V_FC1_WEIGHT_30)
from V_fc1_weight_31 import V_FC1_WEIGHT_31
V_FC1_WEIGHT.append(V_FC1_WEIGHT_31)
from V_fc1_weight_32 import V_FC1_WEIGHT_32
V_FC1_WEIGHT.append(V_FC1_WEIGHT_32)
from V_fc1_weight_33 import V_FC1_WEIGHT_33
V_FC1_WEIGHT.append(V_FC1_WEIGHT_33)
from V_fc1_weight_34 import V_FC1_WEIGHT_34
V_FC1_WEIGHT.append(V_FC1_WEIGHT_34)
from V_fc1_weight_35 import V_FC1_WEIGHT_35
V_FC1_WEIGHT.append(V_FC1_WEIGHT_35)
from V_fc1_weight_36 import V_FC1_WEIGHT_36
V_FC1_WEIGHT.append(V_FC1_WEIGHT_36)
from V_fc1_weight_37 import V_FC1_WEIGHT_37
V_FC1_WEIGHT.append(V_FC1_WEIGHT_37)
from V_fc1_weight_38 import V_FC1_WEIGHT_38
V_FC1_WEIGHT.append(V_FC1_WEIGHT_38)
from V_fc1_weight_39 import V_FC1_WEIGHT_39
V_FC1_WEIGHT.append(V_FC1_WEIGHT_39)
from V_fc1_weight_40 import V_FC1_WEIGHT_40
V_FC1_WEIGHT.append(V_FC1_WEIGHT_40)
from V_fc1_weight_41 import V_FC1_WEIGHT_41
V_FC1_WEIGHT.append(V_FC1_WEIGHT_41)
from V_fc1_weight_42 import V_FC1_WEIGHT_42
V_FC1_WEIGHT.append(V_FC1_WEIGHT_42)
from V_fc1_weight_43 import V_FC1_WEIGHT_43
V_FC1_WEIGHT.append(V_FC1_WEIGHT_43)
from V_fc1_weight_44 import V_FC1_WEIGHT_44
V_FC1_WEIGHT.append(V_FC1_WEIGHT_44)
from V_fc1_weight_45 import V_FC1_WEIGHT_45
V_FC1_WEIGHT.append(V_FC1_WEIGHT_45)
from V_fc1_weight_46 import V_FC1_WEIGHT_46
V_FC1_WEIGHT.append(V_FC1_WEIGHT_46)
from V_fc1_weight_47 import V_FC1_WEIGHT_47
V_FC1_WEIGHT.append(V_FC1_WEIGHT_47)
from V_fc1_weight_48 import V_FC1_WEIGHT_48
V_FC1_WEIGHT.append(V_FC1_WEIGHT_48)
from V_fc1_weight_49 import V_FC1_WEIGHT_49
V_FC1_WEIGHT.append(V_FC1_WEIGHT_49)
from V_fc1_weight_50 import V_FC1_WEIGHT_50
V_FC1_WEIGHT.append(V_FC1_WEIGHT_50)
from V_fc1_weight_51 import V_FC1_WEIGHT_51
V_FC1_WEIGHT.append(V_FC1_WEIGHT_51)
from V_fc1_weight_52 import V_FC1_WEIGHT_52
V_FC1_WEIGHT.append(V_FC1_WEIGHT_52)
from V_fc1_weight_53 import V_FC1_WEIGHT_53
V_FC1_WEIGHT.append(V_FC1_WEIGHT_53)
from V_fc1_weight_54 import V_FC1_WEIGHT_54
V_FC1_WEIGHT.append(V_FC1_WEIGHT_54)
from V_fc1_weight_55 import V_FC1_WEIGHT_55
V_FC1_WEIGHT.append(V_FC1_WEIGHT_55)
from V_fc1_weight_56 import V_FC1_WEIGHT_56
V_FC1_WEIGHT.append(V_FC1_WEIGHT_56)
from V_fc1_weight_57 import V_FC1_WEIGHT_57
V_FC1_WEIGHT.append(V_FC1_WEIGHT_57)
from V_fc1_weight_58 import V_FC1_WEIGHT_58
V_FC1_WEIGHT.append(V_FC1_WEIGHT_58)
from V_fc1_weight_59 import V_FC1_WEIGHT_59
V_FC1_WEIGHT.append(V_FC1_WEIGHT_59)
from V_fc1_weight_60 import V_FC1_WEIGHT_60
V_FC1_WEIGHT.append(V_FC1_WEIGHT_60)
from V_fc1_weight_61 import V_FC1_WEIGHT_61
V_FC1_WEIGHT.append(V_FC1_WEIGHT_61)
from V_fc1_weight_62 import V_FC1_WEIGHT_62
V_FC1_WEIGHT.append(V_FC1_WEIGHT_62)
from V_fc1_weight_63 import V_FC1_WEIGHT_63
V_FC1_WEIGHT.append(V_FC1_WEIGHT_63)
from V_fc1_weight_64 import V_FC1_WEIGHT_64
V_FC1_WEIGHT.append(V_FC1_WEIGHT_64)
from V_fc1_weight_65 import V_FC1_WEIGHT_65
V_FC1_WEIGHT.append(V_FC1_WEIGHT_65)
from V_fc1_weight_66 import V_FC1_WEIGHT_66
V_FC1_WEIGHT.append(V_FC1_WEIGHT_66)
from V_fc1_weight_67 import V_FC1_WEIGHT_67
V_FC1_WEIGHT.append(V_FC1_WEIGHT_67)
from V_fc1_weight_68 import V_FC1_WEIGHT_68
V_FC1_WEIGHT.append(V_FC1_WEIGHT_68)
from V_fc1_weight_69 import V_FC1_WEIGHT_69
V_FC1_WEIGHT.append(V_FC1_WEIGHT_69)
from V_fc1_weight_70 import V_FC1_WEIGHT_70
V_FC1_WEIGHT.append(V_FC1_WEIGHT_70)
from V_fc1_weight_71 import V_FC1_WEIGHT_71
V_FC1_WEIGHT.append(V_FC1_WEIGHT_71)
from V_fc1_weight_72 import V_FC1_WEIGHT_72
V_FC1_WEIGHT.append(V_FC1_WEIGHT_72)
from V_fc1_weight_73 import V_FC1_WEIGHT_73
V_FC1_WEIGHT.append(V_FC1_WEIGHT_73)
from V_fc1_weight_74 import V_FC1_WEIGHT_74
V_FC1_WEIGHT.append(V_FC1_WEIGHT_74)
from V_fc1_weight_75 import V_FC1_WEIGHT_75
V_FC1_WEIGHT.append(V_FC1_WEIGHT_75)
from V_fc1_weight_76 import V_FC1_WEIGHT_76
V_FC1_WEIGHT.append(V_FC1_WEIGHT_76)
from V_fc1_weight_77 import V_FC1_WEIGHT_77
V_FC1_WEIGHT.append(V_FC1_WEIGHT_77)
from V_fc1_weight_78 import V_FC1_WEIGHT_78
V_FC1_WEIGHT.append(V_FC1_WEIGHT_78)
from V_fc1_weight_79 import V_FC1_WEIGHT_79
V_FC1_WEIGHT.append(V_FC1_WEIGHT_79)
from V_fc1_weight_80 import V_FC1_WEIGHT_80
V_FC1_WEIGHT.append(V_FC1_WEIGHT_80)
from V_fc1_weight_81 import V_FC1_WEIGHT_81
V_FC1_WEIGHT.append(V_FC1_WEIGHT_81)
from V_fc1_weight_82 import V_FC1_WEIGHT_82
V_FC1_WEIGHT.append(V_FC1_WEIGHT_82)
from V_fc1_weight_83 import V_FC1_WEIGHT_83
V_FC1_WEIGHT.append(V_FC1_WEIGHT_83)
from V_fc1_weight_84 import V_FC1_WEIGHT_84
V_FC1_WEIGHT.append(V_FC1_WEIGHT_84)
from V_fc1_weight_85 import V_FC1_WEIGHT_85
V_FC1_WEIGHT.append(V_FC1_WEIGHT_85)
from V_fc1_weight_86 import V_FC1_WEIGHT_86
V_FC1_WEIGHT.append(V_FC1_WEIGHT_86)
from V_fc1_weight_87 import V_FC1_WEIGHT_87
V_FC1_WEIGHT.append(V_FC1_WEIGHT_87)
from V_fc1_weight_88 import V_FC1_WEIGHT_88
V_FC1_WEIGHT.append(V_FC1_WEIGHT_88)
from V_fc1_weight_89 import V_FC1_WEIGHT_89
V_FC1_WEIGHT.append(V_FC1_WEIGHT_89)
from V_fc1_weight_90 import V_FC1_WEIGHT_90
V_FC1_WEIGHT.append(V_FC1_WEIGHT_90)
from V_fc1_weight_91 import V_FC1_WEIGHT_91
V_FC1_WEIGHT.append(V_FC1_WEIGHT_91)
from V_fc1_weight_92 import V_FC1_WEIGHT_92
V_FC1_WEIGHT.append(V_FC1_WEIGHT_92)
from V_fc1_weight_93 import V_FC1_WEIGHT_93
V_FC1_WEIGHT.append(V_FC1_WEIGHT_93)
from V_fc1_weight_94 import V_FC1_WEIGHT_94
V_FC1_WEIGHT.append(V_FC1_WEIGHT_94)
from V_fc1_weight_95 import V_FC1_WEIGHT_95
V_FC1_WEIGHT.append(V_FC1_WEIGHT_95)
from V_fc1_weight_96 import V_FC1_WEIGHT_96
V_FC1_WEIGHT.append(V_FC1_WEIGHT_96)
from V_fc1_weight_97 import V_FC1_WEIGHT_97
V_FC1_WEIGHT.append(V_FC1_WEIGHT_97)
from V_fc1_weight_98 import V_FC1_WEIGHT_98
V_FC1_WEIGHT.append(V_FC1_WEIGHT_98)
from V_fc1_weight_99 import V_FC1_WEIGHT_99
V_FC1_WEIGHT.append(V_FC1_WEIGHT_99)
from V_fc1_weight_100 import V_FC1_WEIGHT_100
V_FC1_WEIGHT.append(V_FC1_WEIGHT_100)
from V_fc1_weight_101 import V_FC1_WEIGHT_101
V_FC1_WEIGHT.append(V_FC1_WEIGHT_101)
from V_fc1_weight_102 import V_FC1_WEIGHT_102
V_FC1_WEIGHT.append(V_FC1_WEIGHT_102)
from V_fc1_weight_103 import V_FC1_WEIGHT_103
V_FC1_WEIGHT.append(V_FC1_WEIGHT_103)
from V_fc1_weight_104 import V_FC1_WEIGHT_104
V_FC1_WEIGHT.append(V_FC1_WEIGHT_104)
from V_fc1_weight_105 import V_FC1_WEIGHT_105
V_FC1_WEIGHT.append(V_FC1_WEIGHT_105)
from V_fc1_weight_106 import V_FC1_WEIGHT_106
V_FC1_WEIGHT.append(V_FC1_WEIGHT_106)
from V_fc1_weight_107 import V_FC1_WEIGHT_107
V_FC1_WEIGHT.append(V_FC1_WEIGHT_107)
from V_fc1_weight_108 import V_FC1_WEIGHT_108
V_FC1_WEIGHT.append(V_FC1_WEIGHT_108)
from V_fc1_weight_109 import V_FC1_WEIGHT_109
V_FC1_WEIGHT.append(V_FC1_WEIGHT_109)
from V_fc1_weight_110 import V_FC1_WEIGHT_110
V_FC1_WEIGHT.append(V_FC1_WEIGHT_110)
from V_fc1_weight_111 import V_FC1_WEIGHT_111
V_FC1_WEIGHT.append(V_FC1_WEIGHT_111)
from V_fc1_weight_112 import V_FC1_WEIGHT_112
V_FC1_WEIGHT.append(V_FC1_WEIGHT_112)
from V_fc1_weight_113 import V_FC1_WEIGHT_113
V_FC1_WEIGHT.append(V_FC1_WEIGHT_113)
from V_fc1_weight_114 import V_FC1_WEIGHT_114
V_FC1_WEIGHT.append(V_FC1_WEIGHT_114)
from V_fc1_weight_115 import V_FC1_WEIGHT_115
V_FC1_WEIGHT.append(V_FC1_WEIGHT_115)
from V_fc1_weight_116 import V_FC1_WEIGHT_116
V_FC1_WEIGHT.append(V_FC1_WEIGHT_116)
from V_fc1_weight_117 import V_FC1_WEIGHT_117
V_FC1_WEIGHT.append(V_FC1_WEIGHT_117)
from V_fc1_weight_118 import V_FC1_WEIGHT_118
V_FC1_WEIGHT.append(V_FC1_WEIGHT_118)
from V_fc1_weight_119 import V_FC1_WEIGHT_119
V_FC1_WEIGHT.append(V_FC1_WEIGHT_119)

NN["FC1.WEIGHT".lower()] = torch.Tensor(V_FC1_WEIGHT)

from V_fc1_bias import V_FC1_BIAS
NN["FC1.BIAS".lower()] = torch.Tensor(V_FC1_BIAS)
from V_fc2_weight import V_FC2_WEIGHT
NN["FC2.WEIGHT".lower()] = torch.Tensor(V_FC2_WEIGHT)
from V_fc2_bias import V_FC2_BIAS
NN["FC2.BIAS".lower()] = torch.Tensor(V_FC2_BIAS)
from V_V_weight import V_V_WEIGHT
NN["V.weight"] = torch.Tensor(V_V_WEIGHT)
from V_V_bias import V_V_BIAS
NN["V.bias"] = torch.Tensor(V_V_BIAS)
from V_A_weight import V_A_WEIGHT
NN["A.weight"] = torch.Tensor(V_A_WEIGHT)
from V_A_bias import V_A_BIAS
NN["A.bias"] = torch.Tensor(V_A_BIAS)
