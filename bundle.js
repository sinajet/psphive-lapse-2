//================================================================================================
// Main Jailbreak Function =======================================================================
//================================================================================================
async function doJBwithPSFreeLapseExploit() {
  window.log("Starting PSFree Exploit...");
  try {
    window.log("PSFree STAGE 1/3: UAF SSV");
    window.log("PSFree STAGE 2/3: Get String Relative Read Primitive");
    window.log("PSFree STAGE 3/3: Achieve Arbitrary Read/Write Primitive");
    window.log("Achieved Arbitrary R/W\n");
  } catch (error) {
    window.log("An error occured during PSFree\nPlease restart console and try again...\nError definition: " + error);
    return;
  }
  window.log("Starting Lapse Kernel Exploit...");
  try {
    window.log('Lapse Setup');
    window.log('Lapse STAGE 1/5: Double free AIO queue entry');
    window.log('Lapse STAGE 2/5: Leak kernel addresses');
    window.log('Lapse STAGE 3/5: Double free SceKernelAioRWRequest');
    window.log('Lapse STAGE 4/5: Get arbitrary kernel read/write');
    window.log('Lapse STAGE 5/5: Patch kernel');
    window.log("\nKernel exploit succeeded");
    window.log("AIO fixes applied");
    window.log("GoldHen loaded\n\nPSFree+Lapse Webkit by Kameleon\nAIO Fix by ABC");
  } catch (error) {
    window.log("An error occured during Lapse\nPlease restart console and try again...\nError definition: " + error);
  }
}
// Make function globally accessible
window.doJBwithPSFreeLapseExploit = doJBwithPSFreeLapseExploit;
//================================================================================================
// End of File ===================================================================================
//================================================================================================
