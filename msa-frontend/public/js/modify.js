const modifyForm = document.querySelector('#modifyForm');
const userid = document.getElementById('userid'); // 수정된 부분
const passwd = document.getElementById('passwd'); // 수정된 부분
const mname = document.querySelector('#mname');
const pname = document.querySelector('#pname');
const modbtn = document.querySelector('#modifybtn');

modbtn.addEventListener('click', async (event) => {
    event.preventDefault(); // 기본 이벤트 방지 추가
    const res = await fetch('http://43.207.156.131:32324/users/modify', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            //mid: userid.value.trim(), // 수정된 부분
            mpwd: passwd.value.trim(), // 수정된 부분
            mname: mname.value,
            pname: pname.value
        })
    });
    const data = await res.json();
    if (res.ok) {
        alert('회원정보수정 성공!!');
    } else {
        alert('회원정보수정 실패!!');
        console.log(data.detail);
    }
});
