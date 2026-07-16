window.addEventListener('DOMContentLoaded', function(){
    setInterval(() => {
        const skill_conditions = document.getElementById("skill_conditions");
        skill_conditions.value = "[";

        var skill_conditions_element = document.getElementById("skill_condition");
        let element_count = skill_conditions_element.childElementCount - 1;

        skill_conditions_element = skill_conditions_element.firstElementChild
        skill_condition_all = skill_conditions_element
        
        for(let i = 0; i < element_count; i++){
            if(i != 0){
                skill_conditions.value = skill_conditions.value + ", "
            }

            skill_conditions.value = skill_conditions.value + "{";

            skill_conditions_element = skill_conditions_element.nextElementSibling
            let div = skill_conditions_element.firstElementChild

            let skill_condition_name = div.value
            if(skill_condition_name != ""){
                skill_conditions.value = skill_conditions.value + "\"name\": \"" + skill_condition_name + "\", ";
            }

            div = div.nextElementSibling
            let skill_condition_value = div.value
            if(skill_condition_value !=""){
                skill_conditions.value = skill_conditions.value + "\"value\": \"" + skill_condition_value + "\", ";
            }

            div = div.nextElementSibling
            let skill_condition_option = div.value
            skill_conditions.value = skill_conditions.value + "\"option\": \"" + skill_condition_option + "\"";

            skill_conditions.value = skill_conditions.value + "}"

        }
        skill_conditions.value = skill_conditions.value + "]"
  }, 100);
})

function delete_skill_condition(obj){
    const row = obj.closest("div");
    row.remove();

}

function add_skill_condition(){
    // テーブル取得
    const skill_condition = document.getElementById('skill_condition');

    // 大枠
    let div = document.createElement("div");
    // 技能名作成
    let input_name = document.createElement("input");
    input_name.style.width = "100px";
    div.appendChild(input_name);
    // 数値作成
    let input_value = document.createElement("input");
    input_value.type = "number";
    input_value.style.width = "50px";
    input_value.style.marginLeft = "3px";
    div.appendChild(input_value);
    // 検索タイプ作成
    let select_type = document.createElement("select");
    select_type.style.marginLeft = "3px";
    let option1 = document.createElement("option");
    option1.value = 0; 
    option1.textContent = "一致"; 
    select_type.appendChild(option1);
    let option2 = document.createElement("option");
    option2.value = 1; 
    option2.selected = true; 
    option2.textContent = "以上"; 
    select_type.appendChild(option2);
    let option3 = document.createElement("option");
    option3.value = 2; 
    option3.textContent = "以下"; 
    select_type.appendChild(option3);
    div.appendChild(select_type);
    // 削除ボタン作成
    let button_delete = document.createElement("button");
    button_delete.type = "button";
    button_delete.textContent = "削除";
    button_delete.style.marginLeft = "3px";
    button_delete.style.marginTop = "5px";
    button_delete.setAttribute("onclick", "delete_skill_condition(this)");
    div.appendChild(button_delete);

    skill_condition.appendChild(div);

    // 行作成
    console.log(skill_condition);

    // 行追加
    // skill_condition.appendChild(tr)
}