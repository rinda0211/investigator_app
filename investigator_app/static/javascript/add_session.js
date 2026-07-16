// PL変更処理
function change_PL(PL, PC){
    while(PC.firstElementChild){
        PC.removeChild(PC.firstElementChild)
    }
    let option_first = document.createElement("option");
    PC.appendChild(option_first)
    var investigators = document.getElementById('investigators');
    let investigators_count = investigators.childElementCount;
    investigators = investigators.firstElementChild;
    for(let i = 0; i < investigators_count; i++){
        investigators_element = investigators.firstElementChild;
        let pc_id = investigators_element.value;
        investigators_element = investigators_element.nextElementSibling;
        let pc_name = investigators_element.value;
        investigators_element = investigators_element.nextElementSibling;
        let pc_player = investigators_element.value;

        if(PL.value == pc_player || !PL.value){
            let option = document.createElement("option");
            option.value = pc_id;
            option.textContent = pc_name;
            PC.appendChild(option)
        }
        investigators = investigators.nextElementSibling;
    }
}

// 枠ごと
function change_PL1(){
    const PL1 = document.getElementById('PL1');
    const PC1 = document.getElementById('PC1');
    change_PL(PL1, PC1)
}
function change_PL2(){
    const PL2 = document.getElementById('PL2');
    const PC2 = document.getElementById('PC2');
    change_PL(PL2, PC2)
}
function change_PL3(){
    const PL3 = document.getElementById('PL3');
    const PC3 = document.getElementById('PC3');
    change_PL(PL3, PC3)
}
function change_PL4(){
    const PL4 = document.getElementById('PL4');
    const PC4 = document.getElementById('PC4');
    change_PL(PL4, PC4)
}
function change_PL5(){
    const PL5 = document.getElementById('PL5');
    const PC5 = document.getElementById('PC5');
    change_PL(PL5, PC5)
}
function change_PL6(){
    const PL6 = document.getElementById('PL6');
    const PC6 = document.getElementById('PC6');
    change_PL(PL6, PC6)
}
function change_PL7(){
    const PL7 = document.getElementById('PL7');
    const PC7 = document.getElementById('PC7');
    change_PL(PL7, PC7)
}
function change_PL8(){
    const PL8 = document.getElementById('PL8');
    const PC8 = document.getElementById('PC8');
    change_PL(PL8, PC8)
}
function change_PL9(){
    const PL9 = document.getElementById('PL9');
    const PC9 = document.getElementById('PC9');
    change_PL(PL9, PC9)
}
function change_PL10(){
    const PL10 = document.getElementById('PL10');
    const PC10 = document.getElementById('PC10');
    change_PL(PL10, PC10)
}
function change_KP(){
    const KP = document.getElementById('KP');
    const KPC = document.getElementById('KPC');
    console.log(KP)
    console.log(KPC)
    change_PL(KP, KPC);
}
function change_SKP1(){
    const SKP1 = document.getElementById('SKP1');
    const SKPC1 = document.getElementById('SKPC1');
    change_PL(SKP1, SKPC1)
}
function change_SKP2(){
    const SKP2 = document.getElementById('SKP2');
    const SKPC2 = document.getElementById('SKPC2');
    change_PL(SKP2, SKPC2)
}
function change_SKP3(){
    const SKP3 = document.getElementById('SKP3');
    const SKPC3 = document.getElementById('SKPC3');
    change_PL(SKP3, SKPC3)
}


function change_PC1(){
    PC1 = document.getElementById('PC1')
    PC1_name = document.getElementById('PC1_name')
    PC1_name.value = PC1.options[PC1.selectedIndex].text
    console.log(PC1.options[PC1.selectedIndex].text)
}
function change_PC2(){
    PC2 = document.getElementById('PC2')
    PC2_name = document.getElementById('PC2_name')
    PC2_name.value = PC2.options[PC2.selectedIndex].text
}
function change_PC3(){
    PC3 = document.getElementById('PC3')
    PC3_name = document.getElementById('PC3_name')
    PC3_name.value = PC3.options[PC3.selectedIndex].text
}
function change_PC4(){
    PC4 = document.getElementById('PC4')
    PC4_name = document.getElementById('PC4_name')
    PC4_name.value = PC4.options[PC4.selectedIndex].text
}
function change_PC5(){
    PC5 = document.getElementById('PC5')
    PC5_name = document.getElementById('PC5_name')
    PC5_name.value = PC5.options[PC5.selectedIndex].text
}
function change_PC6(){
    PC6 = document.getElementById('PC6')
    PC6_name = document.getElementById('PC6_name')
    PC6_name.value = PC6.options[PC6.selectedIndex].text
}
function change_PC7(){
    PC7 = document.getElementById('PC7')
    PC7_name = document.getElementById('PC7_name')
    PC7_name.value = PC7.options[PC7.selectedIndex].text
}
function change_PC8(){
    PC8 = document.getElementById('PC8')
    PC8_name = document.getElementById('PC8_name')
    PC8_name.value = PC8.options[PC8.selectedIndex].text
}
function change_PC9(){
    PC9 = document.getElementById('PC9')
    PC9_name = document.getElementById('PC9_name')
    PC9_name.value = PC9.options[PC9.selectedIndex].text
}
function change_PC10(){
    PC10 = document.getElementById('PC10')
    PC10_name = document.getElementById('PC10_name')
    PC10_name.value = PC10.options[PC10.selectedIndex].text
}
function change_KPC(){
    KPC = document.getElementById('KPC')
    KPC_name = document.getElementById('KPC_name')
    KPC_name.value = KPC.options[KPC.selectedIndex].text
}
function change_SKPC1(){
    SKPC1 = document.getElementById('SKPC1')
    SKPC1_name = document.getElementById('SKPC1_name')
    SKPC1_name.value = SKPC1.options[SKPC1.selectedIndex].text
}
function change_SKPC2(){
    SKPC2 = document.getElementById('SKPC2')
    SKPC2_name = document.getElementById('SKPC2_name')
    SKPC2_name.value = SKPC2.options[SKPC2.selectedIndex].text
}
function change_SKPC3(){
    SKPC3 = document.getElementById('SKPC3')
    SKPC3_name = document.getElementById('SKPC3_name')
    SKPC3_name.value = SKPC3.options[SKPC3.selectedIndex].text
}

window.onload = function() {
    PC1 = document.getElementById('PC1').value
    PC2 = document.getElementById('PC2').value
    PC3 = document.getElementById('PC3').value
    PC4 = document.getElementById('PC4').value
    PC5 = document.getElementById('PC5').value
    PC6 = document.getElementById('PC6').value
    PC7 = document.getElementById('PC7').value
    PC8 = document.getElementById('PC8').value
    PC9 = document.getElementById('PC9').value
    PC10 = document.getElementById('PC10').value
    KPC = document.getElementById('KPC').value
    SKPC1 = document.getElementById('SKPC1').value
    SKPC2 = document.getElementById('SKPC2').value
    SKPC3 = document.getElementById('SKPC3').value
    if(PC1) change_PC1()
    else change_PL1()
    if(PC2) change_PC2()
    else change_PL2()
    if(PC3) change_PC3()
    else change_PL3()
    if(PC4) change_PC4()
    else change_PL4()
    if(PC5) change_PC5()
    else change_PL5()
    if(PC6) change_PC6()
    else change_PL6()
    if(PC7) change_PC7()
    else change_PL7()
    if(PC8) change_PC8()
    else change_PL8()
    if(PC9) change_PC9()
    else change_PL9()
    if(PC10) change_PC10()
    else change_PL10()
    if(KPC) change_KPC()
    else change_KP()
    if(SKPC1) change_SKPC1()
    else change_SKP1()
    if(SKPC2) change_SKPC2()
    else change_SKP2()
    if(SKPC3) change_SKPC3()
    else change_SKP3()
}