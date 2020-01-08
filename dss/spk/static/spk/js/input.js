const btnNxt = document.getElementById("btn-nxt")
const btnPrv = document.getElementById("btn-prv")
const btnSbmt = document.getElementById("btn-submit")

const jurusanSekolah = document.getElementById("jurusan-sekolah")

const jurusan = document.getElementById("jurusan")
const ipa = document.querySelectorAll(".ipa") //ipa[0] = sem1, ipa[1] = sem2, ipa[2] = sem3, ipa[3] = sem4, ipa[4] = sem5
const ips = document.querySelectorAll(".ips") //ips[0] = sem1, ips[1] = sem2, ips[2] = sem3, ips[3] = sem4, ips[4] = sem5

const title = document.getElementById("title")

btnNxt.addEventListener("click", ()=>{
    if(jurusanSekolah.value == "IPA"){
        if(!ipa[0].classList.contains("muncul") && !ipa[1].classList.contains("muncul") && !ipa[2].classList.contains("muncul") && !ipa[3].classList.contains("muncul") && !ipa[4].classList.contains("muncul")){
            jurusan.classList.toggle("muncul")
            ipa[0].classList.toggle("muncul")
            btnPrv.classList.toggle("muncul")
            title.innerText = "Nilai Semester 1"
        }
        else if(ipa[0].classList.contains("muncul") && !ipa[1].classList.contains("muncul") && !ipa[2].classList.contains("muncul") && !ipa[3].classList.contains("muncul") && !ipa[4].classList.contains("muncul")){
            title.innerText = "Nilai Semester 2"
            ipa[0].classList.toggle("muncul")
            ipa[1].classList.toggle("muncul")
        }
        else if(!ipa[0].classList.contains("muncul") && ipa[1].classList.contains("muncul") && !ipa[2].classList.contains("muncul") && !ipa[3].classList.contains("muncul") && !ipa[4].classList.contains("muncul")){
            title.innerText = "Nilai Semester 3"
            ipa[1].classList.toggle("muncul")
            ipa[2].classList.toggle("muncul")
        }
        else if(!ipa[0].classList.contains("muncul") && !ipa[1].classList.contains("muncul") && ipa[2].classList.contains("muncul") && !ipa[3].classList.contains("muncul") && !ipa[4].classList.contains("muncul")){
            title.innerText = "Nilai Semester 4"
            ipa[2].classList.toggle("muncul")
            ipa[3].classList.toggle("muncul")
        }
        else if(!ipa[0].classList.contains("muncul") && !ipa[1].classList.contains("muncul") && !ipa[2].classList.contains("muncul") && ipa[3].classList.contains("muncul") && !ipa[4].classList.contains("muncul")){
            title.innerText = "Nilai Semester 5"
            ipa[3].classList.toggle("muncul")
            ipa[4].classList.toggle("muncul")
            btnNxt.classList.toggle("muncul")
            btnSbmt.classList.toggle("muncul")
        }
    }
    else if (jurusanSekolah.value == "IPS"){
        if(!ips[0].classList.contains("muncul") && !ips[1].classList.contains("muncul") && !ips[2].classList.contains("muncul") && !ips[3].classList.contains("muncul") && !ips[4].classList.contains("muncul")){
            jurusan.classList.toggle("muncul")
            ips[0].classList.toggle("muncul")
            btnPrv.classList.toggle("muncul")
            title.innerText = "Nilai Semester 1"
        }
        else if(ips[0].classList.contains("muncul") && !ips[1].classList.contains("muncul") && !ips[2].classList.contains("muncul") && !ips[3].classList.contains("muncul") && !ips[4].classList.contains("muncul")){
            title.innerText = "Nilai Semester 2"
            ips[0].classList.toggle("muncul")
            ips[1].classList.toggle("muncul")
        }
        else if(!ips[0].classList.contains("muncul") && ips[1].classList.contains("muncul") && !ips[2].classList.contains("muncul") && !ips[3].classList.contains("muncul") && !ips[4].classList.contains("muncul")){
            title.innerText = "Nilai Semester 3"
            ips[1].classList.toggle("muncul")
            ips[2].classList.toggle("muncul")
        }
        else if(!ips[0].classList.contains("muncul") && !ips[1].classList.contains("muncul") && ips[2].classList.contains("muncul") && !ips[3].classList.contains("muncul") && !ips[4].classList.contains("muncul")){
            title.innerText = "Nilai Semester 4"
            ips[2].classList.toggle("muncul")
            ips[3].classList.toggle("muncul")
        }
        else if(!ips[0].classList.contains("muncul") && !ips[1].classList.contains("muncul") && !ips[2].classList.contains("muncul") && ips[3].classList.contains("muncul") && !ips[4].classList.contains("muncul")){
            title.innerText = "Nilai Semester 5"
            ips[3].classList.toggle("muncul")
            ips[4].classList.toggle("muncul")
            btnNxt.classList.toggle("muncul")
            btnSbmt.classList.toggle("muncul")
        }
    }
})

btnPrv.addEventListener("click", ()=>{
    if(jurusanSekolah.value == "IPA"){
        if(!jurusan.classList.contains("muncul") && ipa[0].classList.contains("muncul") && !ipa[1].classList.contains("muncul") && !ipa[2].classList.contains("muncul") && !ipa[3].classList.contains("muncul") && !ipa[4].classList.contains("muncul")){
            title.innerText = "Pilih Jurusan SMA"
            ipa[0].classList.toggle("muncul")
            jurusan.classList.toggle("muncul")
            btnPrv.classList.toggle("muncul")
        }
        else if(!ipa[0].classList.contains("muncul") && ipa[1].classList.contains("muncul") && !ipa[2].classList.contains("muncul") && !ipa[3].classList.contains("muncul") && !ipa[4].classList.contains("muncul")){
            title.innerText = "Nilai Semester 1"
            ipa[1].classList.toggle("muncul")
            ipa[0].classList.toggle("muncul")
        }
        else if(!ipa[0].classList.contains("muncul") && !ipa[1].classList.contains("muncul") && ipa[2].classList.contains("muncul") && !ipa[3].classList.contains("muncul") && !ipa[4].classList.contains("muncul")){
            title.innerText = "Nilai Semester 2"
            ipa[2].classList.toggle("muncul")
            ipa[1].classList.toggle("muncul")
        }
        else if(!ipa[0].classList.contains("muncul") && !ipa[1].classList.contains("muncul") && !ipa[2].classList.contains("muncul") && ipa[3].classList.contains("muncul") && !ipa[4].classList.contains("muncul")){
            title.innerText = "Nilai Semester 3"
            ipa[3].classList.toggle("muncul")
            ipa[2].classList.toggle("muncul")
        }
        else if(!ipa[0].classList.contains("muncul") && !ipa[1].classList.contains("muncul") && !ipa[2].classList.contains("muncul") && !ipa[3].classList.contains("muncul") && ipa[4].classList.contains("muncul")){
            title.innerText = "Nilai Semester 4"
            ipa[4].classList.toggle("muncul")
            ipa[3].classList.toggle("muncul")
            btnSbmt.classList.toggle("muncul")
            btnNxt.classList.toggle("muncul")
        }
    }
    else if(jurusanSekolah.value == "IPS"){
        if(!jurusan.classList.contains("muncul") && ips[0].classList.contains("muncul") && !ips[1].classList.contains("muncul") && !ips[2].classList.contains("muncul") && !ips[3].classList.contains("muncul") && !ips[4].classList.contains("muncul")){
            title.innerText = "Pilih Jurusan SMA"
            ips[0].classList.toggle("muncul")
            jurusan.classList.toggle("muncul")
            btnPrv.classList.toggle("muncul")
        }
        else if(!ips[0].classList.contains("muncul") && ips[1].classList.contains("muncul") && !ips[2].classList.contains("muncul") && !ips[3].classList.contains("muncul") && !ips[4].classList.contains("muncul")){
            title.innerText = "Nilai Semester 1"
            ips[1].classList.toggle("muncul")
            ips[0].classList.toggle("muncul")
        }
        else if(!ips[0].classList.contains("muncul") && !ips[1].classList.contains("muncul") && ips[2].classList.contains("muncul") && !ips[3].classList.contains("muncul") && !ips[4].classList.contains("muncul")){
            title.innerText = "Nilai Semester 2"
            ips[2].classList.toggle("muncul")
            ips[1].classList.toggle("muncul")
        }
        else if(!ips[0].classList.contains("muncul") && !ips[1].classList.contains("muncul") && !ips[2].classList.contains("muncul") && ips[3].classList.contains("muncul") && !ips[4].classList.contains("muncul")){
            title.innerText = "Nilai Semester 3"
            ips[3].classList.toggle("muncul")
            ips[2].classList.toggle("muncul")
        }
        else if(!ips[0].classList.contains("muncul") && !ips[1].classList.contains("muncul") && !ips[2].classList.contains("muncul") && !ips[3].classList.contains("muncul") && ips[4].classList.contains("muncul")){
            title.innerText = "Nilai Semester 4"
            ips[4].classList.toggle("muncul")
            ips[3].classList.toggle("muncul")
            btnSbmt.classList.toggle("muncul")
            btnNxt.classList.toggle("muncul")
        }
    }
})