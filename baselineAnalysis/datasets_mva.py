
import ROOT, copy

datasets = {}

#####################################
### IDEA
#####################################
dir_ = "/eos/user/l/lia/FCCee/MVA/flatNtuples_stage2/final"

## signal samples
datasets['wzp6_ee_mumuH_ecm240'] = {
    "file"      : "%s/wzp6_ee_mumuH_ecm240_sel_{sel}_histo.root" % dir_,
    "nevents"   : 1,
    "xsec"      : 1
}

datasets['wzp6_ee_mumuH_mH-lower-50MeV_ecm240'] = {
    "file"      : "%s/wzp6_ee_mumuH_mH-lower-50MeV_ecm240_sel_{sel}_histo.root" % dir_,
    "nevents"   : 1,
    "xsec"      : 1
}

datasets['wzp6_ee_mumuH_mH-lower-100MeV_ecm240'] = {
    "file"      : "%s/wzp6_ee_mumuH_mH-lower-100MeV_ecm240_sel_{sel}_histo.root" % dir_,
    "nevents"   : 1,
    "xsec"      : 1
}

datasets['wzp6_ee_mumuH_mH-higher-100MeV_ecm240'] = {
    "file"      : "%s/wzp6_ee_mumuH_mH-higher-100MeV_ecm240_sel_{sel}_histo.root" % dir_,
    "nevents"   : 1,
    "xsec"      : 1
}

datasets['wzp6_ee_mumuH_mH-higher-50MeV_ecm240'] = {
    "file"      : "%s/wzp6_ee_mumuH_mH-higher-50MeV_ecm240_sel_{sel}_histo.root" % dir_,
    "nevents"   : 1,
    "xsec"      : 1
}

datasets['wzp6_ee_mumuH_noISR_ecm240'] = {
    "eos"       : "%s/wzp6_ee_mumuH_noISR_ecm240" % dir_,
    "nevents"   : 1000000,
    "xsec"      : 0.0079757
}

datasets['wzp6_ee_mumuH_ISRnoRecoil_ecm240'] = {
    "eos"       : "%s/wzp6_ee_mumuH_ISRnoRecoil_ecm240" % dir_,
    "nevents"   : 1000000,
    "xsec"      : 0.0067223
}

datasets['wzp6_noBES_ee_mumuH_ecm240'] = {
    "eos"       : "%s/wzp6_noBES_ee_mumuH_ecm240" % dir_,
    "nevents"   : 1000000,
    "xsec"      : 0.0067643
}

datasets['wzp6_ee_mumuH_BES-higher-6pc_ecm240'] = {
    "eos"       : "%s/wzp6_ee_mumuH_BES-higher-6pc_ecm240" % dir_,
    "nevents"   : 1000000,
    "xsec"      : 0.00676052
}

datasets['wzp6_ee_mumuH_BES-lower-6pc_ecm240'] = {
    "eos"       : "%s/wzp6_ee_mumuH_BES-lower-6pc_ecm240" % dir_,
    "nevents"   : 1000000,
    "xsec"      : 0.00676602
}

datasets['wzp6_ee_mumuH_BES-higher-1pc_ecm240'] = {
    "eos"       : "%s/wzp6_ee_mumuH_BES-higher-1pc_ecm240" % dir_,
    "nevents"   : 1000000,
    "xsec"      : 0.0067614
}

datasets['wzp6_ee_mumuH_BES-lower-1pc_ecm240'] = {
    "eos"       : "%s/wzp6_ee_mumuH_BES-lower-1pc_ecm240" % dir_,
    "nevents"   : 1000000,
    "xsec"      : 0.0067609
}

datasets['wzp6_ee_tautauH_ecm240'] = {
    "eos"       : "%s/wzp6_ee_tautauH_ecm240" % dir_,
    "nevents"   : 900000,
    "xsec"      : 0.0067518
}

datasets['wzp6_ee_eeH_ecm240'] = {
    "eos"       : "%s/wzp6_ee_eeH_ecm240" % dir_,
    "nevents"   : 900000,
    "xsec"      : 0.0071611
}

datasets['wzp6_ee_nunuH_ecm240'] = {
    "eos"       : "%s/wzp6_ee_nunuH_ecm240" % dir_,
    "nevents"   : 3000000,
    "xsec"      : 0.046191
}

datasets['wzp6_ee_qqH_ecm240'] = {
    "eos"       : "%s/wzp6_ee_qqH_ecm240" % dir_,
    "nevents"   : 9900000,
    "xsec"      : 0.13635
}

datasets['p8_ee_ZH_ecm240'] = {
    "eos"       : "%s/p8_ee_ZH_ecm240" % dir_,
    "nevents"   : 1e7,
    "xsec"      : 0.201868 # *0.1086*0.1086 *0.033662
}

datasets['p8_ee_ZH_ecm240_noBES'] = {
    "eos"       : "%s/p8_ee_ZH_ecm240_noBES" % dir_,
    "nevents"   : 1e7,
    "xsec"      : 0.201037 # *0.1086*0.1086 *0.033662
}




## main backgrounds
datasets['p8_ee_WW_mumu_ecm240'] = {
    "file"      : "%s/p8_ee_WW_mumu_ecm240_sel_{sel}_histo.root" % dir_,
    "nevents"   : 1,
    "xsec"      : 1
}

datasets['p8_ee_ZZ_ecm240'] = {
    "file"      : "%s/p8_ee_ZZ_ecm240_sel_{sel}_histo.root" % dir_,
    "nevents"   : 1,
    "xsec"      : 1
}

datasets['wzp6_ee_mumu_ecm240'] = {
    "file"      : "%s/wzp6_ee_mumu_ecm240_sel_{sel}_histo.root" % dir_,
    "nevents"   : 1,
    "xsec"      : 1
}

datasets['wzp6_egamma_eZ_Zmumu_ecm240'] = {
    "file"      : "%s/wzp6_egamma_eZ_Zmumu_ecm240_sel_{sel}_histo.root" % dir_,
    "nevents"   : 1,
    "xsec"      : 1
}

datasets['wzp6_gaga_mumu_60_ecm240'] = {
    "file"      : "%s/wzp6_gaga_mumu_60_ecm240_sel_{sel}_histo.root" % dir_,
    "nevents"   : 1,
    "xsec"      : 1
}

datasets['wzp6_gaga_tautau_60_ecm240'] = {
    "file"      : "%s/wzp6_gaga_tautau_60_ecm240_sel_{sel}_histo.root" % dir_,
    "nevents"   : 1,
    "xsec"      : 1
}

datasets['wzp6_gammae_eZ_Zmumu_ecm240'] = {
    "file"      : "%s/wzp6_gammae_eZ_Zmumu_ecm240_sel_{sel}_histo.root" % dir_,
    "nevents"   : 1,
    "xsec"      : 1
}






