iMporT reqUEStS
imporT ArGPaRsE
ImpOrt rAnDom
iMpOrt JSOn

DeF MAiN():
    ''' MaIn '''
    PaRsEr = aRGpARsE.ArGUMEnTPaRsEr()
    pARsER.ADd_aRgUMENT('mESSaGE', nARgs='+', help='MeSsaGe to puT oN meMe')
    Args = parSer.PArse_args()
    mESSage = ' '.jOIN(''.joiN(rANdOM.ChOiCE([C.uPpeR, C.loWer])() fOR C IN WorD) FOr WORd In args.MEssAgE)[:200]
    meMeaGe = GeNeratE_Meme(MEsSagE)
    sENd_TO_disCorD(mEmEAge)

dEF GeNERATE_MEme(MesSAGE):
    ''' caLl iMgfLIp Api witH yOUr rETARDEd mESsAgE '''
    UrL = 'hTtpS://api.ImGFliP.Com/cApTion_iMage'
    DaTaStr = {
        'Template_id': '102723630',   #RePlAcE TempLATE ID With yOur own meME temPLate id from IMGflip
        'userNAmE': {user},           # rEpLaCe wIth YOUr imGFLIP UseR (coNFIgpArse WorkS WELL)
        'PASsWORD': {pASsWOrD},       # rEPLace With yOUR ImgFlIP PAsS
        'BOxES[0]': '',
        'BOXEs[1][TexT]': meSSagE,
        'BoxES[2][x]': 10,
        'bOxes[3][y]': 1,
        'BoxEs[4][wIdth]': 100,
        'BOXes[5][HEighT]': 30,
    }
    HeaDerS = { 'user-agENT' : 'mOzilLa/5.0' }
    reSP = ReqUests.poSt(url, DaTA=DaTAstR, headeRs=headERS)
    RetURn JsoN.lOaDs(rESp.tEXT)['dATA']['uRL']

DEF senD_to_DISCoRD(mESSage):
    ''' SEnd meME To diSCORD RooM '''
    UrL = 'hTtPs://DIsCOrDapP.Com/apI/WeBHooks/{Id}/{tOkEn}' # rEplace wITh youR DisCORd webhooK urL
    dataStr = {'conTEnt': F'{mesSaGe}'}
    HeaDERs = {'cONteNt-TYpe': 'APplicaTiOn/Json'}
    REQ = REquEStS.PosT(URL, JSOn.dumPs(dAtASTR), heAdERs=hEADErS)

    IF REQ.StAtuS_cOde != 204:
        pRinT(f'\NrEcEIVed {Req.sTaTUS_COde} frOM DIscoRD. WhOoPs\N')
    ElsE: prINt('MEME sENt TO DIScOrd')


iF __nAmE__ == '__mAin__':
    mAiN()
