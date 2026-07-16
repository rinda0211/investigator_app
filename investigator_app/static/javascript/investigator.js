window.addEventListener('DOMContentLoaded', function(){
    setInterval(() => {
        var str = Number(document.getElementById('str').value);
        var con = Number(document.getElementById('con').value);
        var pow = Number(document.getElementById('pow').value);
        var dex = Number(document.getElementById('dex').value);
        var app = Number(document.getElementById('app').value);
        var siz = Number(document.getElementById('siz').value);
        var int = Number(document.getElementById('int').value);
        var edu = Number(document.getElementById('edu').value);
        var hp = document.getElementById('hp');
        var mp = document.getElementById('mp');
        var san = document.getElementById('san');
        var ide = document.getElementById('ide');
        var luck = document.getElementById('luck');
        var knowledge = document.getElementById('knowledge');
        
        var str_add = Number(document.getElementById('str_add').value);
        var con_add = Number(document.getElementById('con_add').value);
        var pow_add = Number(document.getElementById('pow_add').value);
        var dex_add = Number(document.getElementById('dex_add').value);
        var app_add = Number(document.getElementById('app_add').value);
        var siz_add = Number(document.getElementById('siz_add').value);
        var int_add = Number(document.getElementById('int_add').value);
        var edu_add = Number(document.getElementById('edu_add').value);
        var hp_add = Number(document.getElementById('hp_add').value);
        var mp_add = Number(document.getElementById('mp_add').value);
        var san_add = Number(document.getElementById('san_add').value);
        var ide_add = Number(document.getElementById('ide_add').value);
        var luck_add = Number(document.getElementById('luck_add').value);
        var knowledge_add = Number(document.getElementById('knowledge_add').value);
        
        var str_tmp = Number(document.getElementById('str_tmp').value);
        var con_tmp = Number(document.getElementById('con_tmp').value);
        var pow_tmp = Number(document.getElementById('pow_tmp').value);
        var dex_tmp = Number(document.getElementById('dex_tmp').value);
        var app_tmp = Number(document.getElementById('app_tmp').value);
        var siz_tmp = Number(document.getElementById('siz_tmp').value);
        var int_tmp = Number(document.getElementById('int_tmp').value);
        var edu_tmp = Number(document.getElementById('edu_tmp').value);
        var hp_tmp = Number(document.getElementById('hp_tmp').value);
        var mp_tmp = Number(document.getElementById('mp_tmp').value);
        var san_tmp = Number(document.getElementById('san_tmp').value);
        var ide_tmp = Number(document.getElementById('ide_tmp').value);
        var luck_tmp = Number(document.getElementById('luck_tmp').value);
        var knowledge_tmp = Number(document.getElementById('knowledge_add').value);
        
        var str_sum = document.getElementById('str_sum');
        var con_sum = document.getElementById('con_sum');
        var pow_sum = document.getElementById('pow_sum');
        var dex_sum = document.getElementById('dex_sum');
        var app_sum = document.getElementById('app_sum');
        var siz_sum = document.getElementById('siz_sum');
        var int_sum = document.getElementById('int_sum');
        var edu_sum = document.getElementById('edu_sum');
        var hp_sum = document.getElementById('hp_sum');
        var mp_sum = document.getElementById('mp_sum');
        var san_sum = document.getElementById('san_sum');
        var ide_sum = document.getElementById('ide_sum');
        var luck_sum = document.getElementById('luck_sum');
        var knowledge_sum = document.getElementById('knowledge_sum');

        str_sum.value = str + str_add + str_tmp;
        con_sum.value = con + con_add + con_tmp;
        pow_sum.value = pow + pow_add + pow_tmp;
        dex_sum.value = dex + dex_add + dex_tmp;
        app_sum.value = app + app_add + app_tmp;
        siz_sum.value = siz + siz_add + siz_tmp;
        int_sum.value = int + int_add + int_tmp;
        edu_sum.value = edu + edu_add + edu_tmp;

        hp.value = Math.ceil((Number(con_sum.value) + Number(siz_sum.value))/2);
        mp.value = Number(pow_sum.value);
        san.value = Number(pow_sum.value) * 5;
        ide.value = Number(int_sum.value) * 5;
        luck.value = Number(pow_sum.value) * 5;
        knowledge.value = Number(edu_sum.value) * 5;

        hp_sum.value = Number(hp.value) + hp_add + hp_tmp
        mp_sum.value = Number(mp.value) + mp_add + mp_tmp
        san_sum.value = Number(san.value) + san_add + san_tmp
        ide_sum.value = Number(ide.value) + ide_add + ide_tmp
        luck_sum.value = Number(luck.value) + luck_add + luck_tmp
        knowledge_sum.value = Number(knowledge.value) + knowledge_add + knowledge_tmp

        let db = Number(str_sum.value) + Number(siz_sum.value);
        var damage_bonus = document.getElementById('damage_bonus');
        if(db <= 12){damage_bonus.value = "-1d6";}
        else if(db <= 16){damage_bonus.value = "-1d4";}
        else if(db <= 24){damage_bonus.value = "0";}
        else if(db <= 32){damage_bonus.value = "+1d4";}
        else if(db <= 40){damage_bonus.value = "+1d6";}
        else{
            db = Math.floor((db - 41)/16) + 2;
            damage_bonus.value = "+" + db + "d6"
        }

        let cal_type = document.getElementById('cal_type').value
        var job_point = document.getElementById('job_point');
        let job_point_add = document.getElementById('job_point_add').value;
        let job_point_max = 0;
        if(cal_type == 0){job_point_max = Number(edu_sum.value) * 20;}
        else if(cal_type == 1){job_point_max = Number(edu_sum.value) * 10 + Number(str_sum.value) * 10;}
        else if(cal_type == 2){job_point_max = Number(edu_sum.value) * 10 + Number(con_sum.value) * 10;}
        else if(cal_type == 3){job_point_max = Number(edu_sum.value) * 10 + Number(pow_sum.value) * 10;}
        else if(cal_type == 4){job_point_max = Number(edu_sum.value) * 10 + Number(dex_sum.value) * 10;}
        else if(cal_type == 5){job_point_max = Number(edu_sum.value) * 10 + Number(app_sum.value) * 10;}
        else if(cal_type == 6){job_point_max = Number(edu_sum.value) * 10 + Number(siz_sum.value) * 10;}
        else if(cal_type == 7){job_point_max = Number(edu_sum.value) * 10 + Number(int_sum.value) * 10;}
        job_point_max = job_point_max + job_point_add

        job_point.value = "0/" + Number(job_point_max)

        var interest_point = document.getElementById('interest_point');
        let interest_point_max = 0;
        interest_point_max = Number(int_sum.value) * 10;
        let interest_point_add = document.getElementById('interest_point_add').value;
        interest_point_max = interest_point_max + interest_point_add

        interest_point.value = "0/" + Number(interest_point_max)

        // 戦闘技能処理
        const battle_skills_json = document.getElementById('battle_skills_json');
        battle_skills_json.value = "[";

        const battle_skills = document.querySelector(".battle_skills").firstElementChild;
        let battle_skills_count = battle_skills.childElementCount - 1;
        var skill = battle_skills.firstElementChild;
        for(let i = 0; i < battle_skills_count; i++){
            if(i != 0){
                battle_skills_json.value = battle_skills_json.value + ", "
            }

            skill = skill.nextElementSibling;
            var skill_element = skill.firstElementChild;
            var skill_check = skill_element.firstElementChild;
            skill_element = skill_element.nextElementSibling;
            var skill_name = skill_element.firstElementChild;
            skill_element = skill_element.nextElementSibling;
            var skill_initial = skill_element.firstElementChild;
            skill_element = skill_element.nextElementSibling;
            var skill_job = skill_element.firstElementChild;
            skill_element = skill_element.nextElementSibling;
            var skill_interest = skill_element.firstElementChild;
            skill_element = skill_element.nextElementSibling;
            var skill_growth = skill_element.firstElementChild;
            skill_element = skill_element.nextElementSibling;
            var skill_others = skill_element.firstElementChild;
            skill_element = skill_element.nextElementSibling;
            var skill_sum = skill_element.firstElementChild;
            skill_sum.value = Number(skill_initial.value) + Number(skill_job.value) + Number(skill_interest.value) + Number(skill_growth.value) + Number(skill_others.value);

            battle_skills_json.value = battle_skills_json.value + "{\"id\": " + skill_check.value +", ";
            battle_skills_json.value = battle_skills_json.value + "\"name\": \"" + skill_name.value + "\", ";
            battle_skills_json.value = battle_skills_json.value + "\"spell\": \"" + skill_name.value + "\", ";
            battle_skills_json.value = battle_skills_json.value + "\"points\": {"
            battle_skills_json.value = battle_skills_json.value + "\"initial_points\": " + skill_initial.value + ", ";
            battle_skills_json.value = battle_skills_json.value + "\"job_points\": " + skill_job.value + ", ";
            battle_skills_json.value = battle_skills_json.value + "\"interest_points\": " + skill_interest.value + ", ";
            battle_skills_json.value = battle_skills_json.value + "\"growth_points\": " + skill_growth.value + ", ";
            battle_skills_json.value = battle_skills_json.value + "\"others_points\": " + skill_others.value;
            battle_skills_json.value = battle_skills_json.value + "}}"
        }
        battle_skills_json.value = battle_skills_json.value + "]";
        console.log(battle_skills_json.value);
        // 探索技能処理
        const search_skills_json = document.getElementById('search_skills_json');
        search_skills_json.value = "[";

        const search_skills = document.querySelector(".search_skills").firstElementChild;
        let search_skills_count = search_skills.childElementCount - 1;
        var skill = search_skills.firstElementChild;
        for(let i = 0; i < search_skills_count; i++){
            if(i != 0){
                search_skills_json.value = search_skills_json.value + ", "
            }

            skill = skill.nextElementSibling;
            var skill_element = skill.firstElementChild;
            var skill_check = skill_element.firstElementChild;
            skill_element = skill_element.nextElementSibling;
            var skill_name = skill_element.firstElementChild;
            skill_element = skill_element.nextElementSibling;
            var skill_initial = skill_element.firstElementChild;
            skill_element = skill_element.nextElementSibling;
            var skill_job = skill_element.firstElementChild;
            skill_element = skill_element.nextElementSibling;
            var skill_interest = skill_element.firstElementChild;
            skill_element = skill_element.nextElementSibling;
            var skill_growth = skill_element.firstElementChild;
            skill_element = skill_element.nextElementSibling;
            var skill_others = skill_element.firstElementChild;
            skill_element = skill_element.nextElementSibling;
            var skill_sum = skill_element.firstElementChild;
            skill_sum.value = Number(skill_initial.value) + Number(skill_job.value) + Number(skill_interest.value) + Number(skill_growth.value) + Number(skill_others.value);

            search_skills_json.value = search_skills_json.value + "{\"id\": " + skill_check.value +", ";
            search_skills_json.value = search_skills_json.value + "\"name\": \"" + skill_name.value + "\", ";
            search_skills_json.value = search_skills_json.value + "\"points\": {"
            search_skills_json.value = search_skills_json.value + "\"initial_points\": " + skill_initial.value + ", ";
            search_skills_json.value = search_skills_json.value + "\"job_points\": " + skill_job.value + ", ";
            search_skills_json.value = search_skills_json.value + "\"interest_points\": " + skill_interest.value + ", ";
            search_skills_json.value = search_skills_json.value + "\"growth_points\": " + skill_growth.value + ", ";
            search_skills_json.value = search_skills_json.value + "\"others_points\": " + skill_others.value;
            search_skills_json.value = search_skills_json.value + "}}";
        }
        search_skills_json.value = search_skills_json.value + "]";
        console.log(search_skills_json.value);
        // 行動技能処理
        const action_skills_json = document.getElementById('action_skills_json');
        action_skills_json.value = "[";

        const action_skills = document.querySelector(".action_skills").firstElementChild;
        let action_skills_count = action_skills.childElementCount - 1;
        var skill = action_skills.firstElementChild;
        for(let i = 0; i < action_skills_count; i++){
            if(i != 0){
                action_skills_json.value = action_skills_json.value + ", "
            }

            skill = skill.nextElementSibling;
            var skill_element = skill.firstElementChild;
            var skill_check = skill_element.firstElementChild;
            skill_element = skill_element.nextElementSibling;
            var skill_name = skill_element.firstElementChild;
            skill_element = skill_element.nextElementSibling;
            var skill_initial = skill_element.firstElementChild;
            skill_element = skill_element.nextElementSibling;
            var skill_job = skill_element.firstElementChild;
            skill_element = skill_element.nextElementSibling;
            var skill_interest = skill_element.firstElementChild;
            skill_element = skill_element.nextElementSibling;
            var skill_growth = skill_element.firstElementChild;
            skill_element = skill_element.nextElementSibling;
            var skill_others = skill_element.firstElementChild;
            skill_element = skill_element.nextElementSibling;
            var skill_sum = skill_element.firstElementChild;
            skill_sum.value = Number(skill_initial.value) + Number(skill_job.value) + Number(skill_interest.value) + Number(skill_growth.value) + Number(skill_others.value);

            action_skills_json.value = action_skills_json.value + "{\"id\": " + skill_check.value +", ";
            action_skills_json.value = action_skills_json.value + "\"name\": \"" + skill_name.value + "\", ";
            action_skills_json.value = action_skills_json.value + "\"points\": {"
            action_skills_json.value = action_skills_json.value + "\"initial_points\": " + skill_initial.value + ", ";
            action_skills_json.value = action_skills_json.value + "\"job_points\": " + skill_job.value + ", ";
            action_skills_json.value = action_skills_json.value + "\"interest_points\": " + skill_interest.value + ", ";
            action_skills_json.value = action_skills_json.value + "\"growth_points\": " + skill_growth.value + ", ";
            action_skills_json.value = action_skills_json.value + "\"others_points\": " + skill_others.value;
            action_skills_json.value = action_skills_json.value + "}}";
        }
        action_skills_json.value = action_skills_json.value + "]";
        console.log(action_skills_json.value);
        // 交渉技能処理
        const interpersonal_skills_json = document.getElementById('interpersonal_skills_json');
        interpersonal_skills_json.value = "[";

        const interpersonal_skills = document.querySelector(".interpersonal_skills").firstElementChild;
        let interpersonal_skills_count = interpersonal_skills.childElementCount - 1;
        var skill = interpersonal_skills.firstElementChild;
        for(let i = 0; i < interpersonal_skills_count; i++){
            if(i != 0){
                interpersonal_skills_json.value = interpersonal_skills_json.value + ", "
            }

            skill = skill.nextElementSibling;
            var skill_element = skill.firstElementChild;
            var skill_check = skill_element.firstElementChild;
            skill_element = skill_element.nextElementSibling;
            var skill_name = skill_element.firstElementChild;
            skill_element = skill_element.nextElementSibling;
            var skill_initial = skill_element.firstElementChild;
            skill_element = skill_element.nextElementSibling;
            var skill_job = skill_element.firstElementChild;
            skill_element = skill_element.nextElementSibling;
            var skill_interest = skill_element.firstElementChild;
            skill_element = skill_element.nextElementSibling;
            var skill_growth = skill_element.firstElementChild;
            skill_element = skill_element.nextElementSibling;
            var skill_others = skill_element.firstElementChild;
            skill_element = skill_element.nextElementSibling;
            var skill_sum = skill_element.firstElementChild;
            skill_sum.value = Number(skill_initial.value) + Number(skill_job.value) + Number(skill_interest.value) + Number(skill_growth.value) + Number(skill_others.value);

            interpersonal_skills_json.value = interpersonal_skills_json.value + "{\"id\": " + skill_check.value +", ";
            interpersonal_skills_json.value = interpersonal_skills_json.value + "\"name\": \"" + skill_name.value + "\", ";
            interpersonal_skills_json.value = interpersonal_skills_json.value + "\"points\": {"
            interpersonal_skills_json.value = interpersonal_skills_json.value + "\"initial_points\": " + skill_initial.value + ", ";
            interpersonal_skills_json.value = interpersonal_skills_json.value + "\"job_points\": " + skill_job.value + ", ";
            interpersonal_skills_json.value = interpersonal_skills_json.value + "\"interest_points\": " + skill_interest.value + ", ";
            interpersonal_skills_json.value = interpersonal_skills_json.value + "\"growth_points\": " + skill_growth.value + ", ";
            interpersonal_skills_json.value = interpersonal_skills_json.value + "\"others_points\": " + skill_others.value;
            interpersonal_skills_json.value = interpersonal_skills_json.value + "}}";
        }
        interpersonal_skills_json.value = interpersonal_skills_json.value + "]";
        console.log(interpersonal_skills_json.value);
        // 知識技能処理
        const knowledge_skills_json = document.getElementById('knowledge_skills_json');
        knowledge_skills_json.value = "[";

        const knowledge_skills = document.querySelector(".knowledge_skills").firstElementChild;
        let knowledge_skills_count = knowledge_skills.childElementCount - 1;
        var skill = knowledge_skills.firstElementChild;
        for(let i = 0; i < knowledge_skills_count; i++){
            if(i != 0){
                knowledge_skills_json.value = knowledge_skills_json.value + ", "
            }

            skill = skill.nextElementSibling;
            var skill_element = skill.firstElementChild;
            var skill_check = skill_element.firstElementChild;
            skill_element = skill_element.nextElementSibling;
            var skill_name = skill_element.firstElementChild;
            skill_element = skill_element.nextElementSibling;
            var skill_initial = skill_element.firstElementChild;
            skill_element = skill_element.nextElementSibling;
            var skill_job = skill_element.firstElementChild;
            skill_element = skill_element.nextElementSibling;
            var skill_interest = skill_element.firstElementChild;
            skill_element = skill_element.nextElementSibling;
            var skill_growth = skill_element.firstElementChild;
            skill_element = skill_element.nextElementSibling;
            var skill_others = skill_element.firstElementChild;
            skill_element = skill_element.nextElementSibling;
            var skill_sum = skill_element.firstElementChild;
            skill_sum.value = Number(skill_initial.value) + Number(skill_job.value) + Number(skill_interest.value) + Number(skill_growth.value) + Number(skill_others.value);

            knowledge_skills_json.value = knowledge_skills_json.value + "{\"id\": " + skill_check.value +", ";
            knowledge_skills_json.value = knowledge_skills_json.value + "\"name\": \"" + skill_name.value + "\", ";
            knowledge_skills_json.value = knowledge_skills_json.value + "\"points\": {"
            knowledge_skills_json.value = knowledge_skills_json.value + "\"initial_points\": " + skill_initial.value + ", ";
            knowledge_skills_json.value = knowledge_skills_json.value + "\"job_points\": " + skill_job.value + ", ";
            knowledge_skills_json.value = knowledge_skills_json.value + "\"interest_points\": " + skill_interest.value + ", ";
            knowledge_skills_json.value = knowledge_skills_json.value + "\"growth_points\": " + skill_growth.value + ", ";
            knowledge_skills_json.value = knowledge_skills_json.value + "\"others_points\": " + skill_others.value;
            knowledge_skills_json.value = knowledge_skills_json.value + "}}";
        }
        knowledge_skills_json.value = knowledge_skills_json.value + "]";
        console.log(knowledge_skills_json.value);

        // SAN値
        let cm_initial_points = Number(document.getElementById('cthulhu_mythos_initial_points').value)
        let cm_job_points = Number(document.getElementById('cthulhu_mythos_job_points').value)
        let cm_interest_points = Number(document.getElementById('cthulhu_mythos_interest_points').value)
        let cm_growth_points = Number(document.getElementById('cthulhu_mythos_growth_points').value)
        let cm_others_points = Number(document.getElementById('cthulhu_mythos_others_points').value)
        let cm_sum_points = cm_initial_points + cm_job_points + cm_interest_points + cm_growth_points + cm_others_points

        var san_max = document.getElementById('san_max');
        san_max.value = 99 - cm_sum_points;

        var ind_ins = document.getElementById('ind_ins');
        ind_ins.value = Math.floor(Number(san_max.value) * 4 / 5);
  }, 10);
})

function delete_skills(obj){
    const row = obj.closest("tr");
    row.remove();
}

function add_skills(){
    // 行作成
    let tr = document.createElement("tr");

    // id列作成
    let td_id = document.createElement("td");
    let input_id = document.createElement("input");
    input_id.type = "checkbox";
    input_id.value = 0;
    td_id.appendChild(input_id);
    tr.appendChild(td_id);

    // 技能名列作成
    let th_name = document.createElement("th");
    th_name.scope = "row"
    th_name.style="font-size: 15px; font-weight: normal;"
    let input_name = document.createElement("input");
    input_name.style="width: 150px; border: 0px; text-align: center;"
    th_name.appendChild(input_name);
    tr.appendChild(th_name);

    // 初期値列作成
    let td_initial = document.createElement("td");
    let input_initial = document.createElement("input");
    input_initial.type = "number";
    input_initial.value = 0;
    input_initial.style = "width: 50px;";
    td_initial.appendChild(input_initial);
    tr.appendChild(td_initial);

    // 職業P列作成
    let td_job = document.createElement("td");
    let input_job = document.createElement("input");
    input_job.type = "number";
    input_job.value = 0;
    input_job.style = "width: 50px;";
    td_job.appendChild(input_job);
    tr.appendChild(td_job);

    // 興味P列作成
    let td_interest = document.createElement("td");
    let input_interest = document.createElement("input");
    input_interest.type = "number";
    input_interest.value = 0;
    input_interest.style = "width: 50px;";
    td_interest.appendChild(input_interest);
    tr.appendChild(td_interest);

    // 成長P列作成
    let td_growth = document.createElement("td");
    let input_growth = document.createElement("input");
    input_growth.type = "number";
    input_growth.value = 0;
    input_growth.style = "width: 50px;";
    td_growth.appendChild(input_growth);
    tr.appendChild(td_growth);

    // その他P列作成
    let td_others = document.createElement("td");
    let input_others = document.createElement("input");
    input_others.type = "number";
    input_others.value = 0;
    input_others.style = "width: 50px;";
    td_others.appendChild(input_others);
    tr.appendChild(td_others);

    // 合計P列作成
    let td_sum = document.createElement("td");
    let input_sum = document.createElement("input");
    input_sum.type = "number";
    input_sum.value = 0;
    input_sum.style = "width: 50px;";
    input_sum.disabled = true;
    td_sum.appendChild(input_sum);
    tr.appendChild(td_sum);

    // 削除ボタン作成
    let td_delete = document.createElement("td");
    let button_delete = document.createElement("button");
    button_delete.type = "button";
    button_delete.textContent = "削除";
    button_delete.setAttribute("onclick", "delete_skills(this)");
    td_delete.appendChild(button_delete)
    tr.appendChild(td_delete)

    return tr;
}

function add_battle_skills(){
    // テーブル取得
    const battle_skills_table = document.getElementById('battle_skills_table').firstElementChild;

    // 行作成
    tr = add_skills();

    // 行追加
    battle_skills_table.appendChild(tr)
}

function add_search_skills(){
    // テーブル取得
    const search_skills_table = document.getElementById('search_skills_table').firstElementChild;

    // 行作成
    tr = add_skills();

    // 行追加
    search_skills_table.appendChild(tr)
}

function add_action_skills(){
    // テーブル取得
    const action_skills_table = document.getElementById('action_skills_table').firstElementChild;

    // 行作成
    tr = add_skills();

    // 行追加
    action_skills_table.appendChild(tr)
}

function add_interpersonal_skills(){
    // テーブル取得
    const interpersonal_skills_table = document.getElementById('interpersonal_skills_table').firstElementChild;

    // 行作成
    tr = add_skills();

    // 行追加
    interpersonal_skills_table.appendChild(tr)
}

function add_knowledge_skills(){
    // テーブル取得
    const knowledge_skills_table = document.getElementById('knowledge_skills_table').firstElementChild;

    // 行作成
    tr = add_skills();

    // 行追加
    knowledge_skills_table.appendChild(tr)
}