<style scoped>
::-webkit-scrollbar {
  width: 10px;
}

::-webkit-scrollbar-track {
  background: #f1f1f1;
}

::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 5px;
}

::-webkit-scrollbar-thumb:hover {
  background: #555;
}

* {
  scrollbar-width: none;
  /* 设置滚动条宽度：auto | thin | none */
  scrollbar-color: #888 #f1f1f1;
}

.logo img {
  transition: transform 1.5s linear;
}

.logo:hover img {
  transform: rotate(360deg);
}

.spliter {
  color: #ffffff;
  margin-right: 3px;
}

.split-quote svg {
  width: 160px;
  height: 20px;
}

.footer {
  margin-top: 10px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: row;
}

.rotate-initial {
  transform: rotate(-45deg);
  transition: transform 1s;
}

.rotated {
  transform: rotate(315deg);
  /* 45 + 360 */
  transition: transform 1s;
}

.advice-container {
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  font-family: "Manrope", sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  width: 195px;
  height: auto;
  background-color: rgba(49, 58, 73, 0.3);
  border-radius: 10px;
  overflow: hidden;
  margin-top: 10px;
}

.paragraph {
  font-size: 17px;
  background-image: linear-gradient(to right, hsl(150, 100%, 66%), #C031B5);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  text-transform: uppercase;
  font-weight: 500;
  letter-spacing: 1px;
}

.advice-details {
  color: hsl(193, 38%, 86%);
  font-size: 15px;
  font-weight: 500;
  line-height: 25px;
  text-wrap: balance;
  letter-spacing: 1px;
  overflow-y:hidden;
}


.quote {
  align-items: center;
  display: flex;
  justify-content: center;
  height: 25px;
  width: 55px;
  border-radius: 74%;
  background-color: transparent;
  border: none;
  cursor: pointer;
  transition: 0.3s all;
}

.value.active {
  background-color: #1a1f24;
  outline: none;
  margin-left: 7px;
}

.value.active::before {
  opacity: 1;
}

.menu-title {
  color: #ffffff;
  font-size: 18px;
  margin-top: 10px;
  margin-bottom: 7px;
}

.input {
  display: flex;
  flex-direction: column;
  width: 200px;
  background-color: #2C2C2F;
  justify-content: center;
  justify-items: center;
  border-radius: 10px;
  transition: 0.7s;
  padding: 10px;
  overflow: hidden;
  position: fixed;
  top: 3px;
  left: 3px;
  height: 100vh;
  z-index: 1000;
}

.background-layer {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: -1;
  background: no-repeat center/cover;
  transition: background-image 1s ease-in-out;
}

.content-layer {
  position: relative;
  z-index: 0;
  overflow-y: auto;
  height: 100vh;
}

.value {
  font-size: 15px;
  background-color: transparent;
  border: none;
  padding: 10px;
  color: white;
  display: flex;
  position: relative;
  gap: 5px;
  cursor: pointer;
  border-radius: 10px;
  transition: 0.7s;
  box-sizing: border-box;
}

.value:not(:active):hover,
.value:focus {
  display: flex;
  box-sizing: border-box;
  border: 2px solid #1a1f24;
  color: #637185;
}

.value:focus,
.value:active {
  background-color: #1a1f24;
  outline: none;
  margin-left: 17px;
}

.value::before {
  content: "";
  position: absolute;
  top: 5px;
  left: -15px;
  width: 5px;
  height: 80%;
  background-color: #2f81f7;
  border-radius: 5px;
  opacity: 0;
  transition: 0.7s;
}

.value:focus::before,
.value:active::before {
  opacity: 1;
}

.value svg {
  width: 20px;
}
</style>

<template>
  <div class="background-layer" :style="{ backgroundImage: `url(${backgroundImage})` }">
    <div class="content-layer" ref="contentLayer">
      <div class="input">
        <div class='logo' align='center'><img src="@/assets/pngs/logo.png" style="width:100px;height:100px;  "></img>
        </div>
        <div style="display: flex; justify-content: center; align-items: center; ">
          <seven-segment-clock />
        </div>
        <!-- 每日格言 -->
        <div class="advice-container">
          <p class="paragraph">Q U O T E </p> 
          <div class="advice-details">{{ quote_content }}</div>
          <div class="split-quote">
            <svg t="1741586765537" class="icon" viewBox="0 0 11051 1024" version="1.1"
              xmlns="http://www.w3.org/2000/svg" p-id="6414" width="200" height="30">
              <path
                d="M3960.801743 519.520675c-68.830838 3.072029-135.459089 6.144058-202.08734 9.042198-245.58843 10.665157-491.205842 21.127445-736.794272 31.96649-223.330711 9.853678-446.63244 20.373928-669.992132 29.47409-17.128011 0.695554-34.63278-7.41924-51.934678-11.5346-59.469844-14.200889-118.823762-28.807517-178.409532-42.515721-20.808649-4.781932-42.109982-7.390258-63.875018-11.099879v-44.660346c52.717177-10.056548 104.941669-19.678374 156.992273-30.11168 24.141511-4.839895 49.326352-8.056831 71.642035-17.562732 61.295673-26.141228 124.214304-12.346079 186.176549-9.969603 207.477882 7.969887 414.86882 18.403192 622.288738 28.111963 260.658761 12.201172 521.28854 24.721139 781.91832 36.748422 27.590298 1.275182 55.325503 0.173888 84.046076 0.173889l0.028981 31.937509zM7064.217587 521.955113v-30.488439c54.745875-2.724252 108.564345-5.535448 162.382815-8.027849 205.738998-9.534882 411.477995-18.953839 617.216993-28.430759 274.04817-12.635893 548.125322-25.300767 822.173492-37.878697 7.129426-0.318795 14.548666-1.072312 21.359296 0.434721 89.117822 19.678374 178.177681 39.733507 267.23754 59.701696 3.014066 0.666572 5.97017 1.680922 10.143491 2.89814V524.563439c-47.355617 8.752384-96.015396 15.707922-143.602864 27.126596-39.936377 9.592845-78.539609 24.75012-117.983301 36.574534-8.781366 2.637308-18.635044 2.724252-27.938075 2.318512-193.045142-8.404608-386.090284-17.099029-579.135426-25.648544-324.910537-14.345796-649.850055-28.691591-974.789574-42.863499-18.113378-0.811479-36.28472-0.115926-57.064387-0.115925zM6114.294059 673.209068c-23.561883-78.713497-82.249229-124.996802-146.095265-170.72946 59.962528-46.660063 114.882291-96.71095 148.761555-167.947244l488.887329 128.88031-5.042765 84.799592-486.510854 124.996802zM4421.403221 462.775083l485.583449-128.184757c33.966207 68.801857 86.364588 121.084312 149.659978 166.990859-62.744743 46.167379-123.257918 91.813093-146.240172 171.425013-57.788923-14.693573-114.592477-29.06835-171.33807-43.588034-98.536779-25.213823-196.92865-50.920329-295.610336-75.46758-16.635327-4.144341-24.112529-10.375343-22.460589-28.517703 1.796847-19.446523 0.40574-39.211842 0.40574-62.657798zM1758.475759 487.496222c5.071746 21.127445 2.144624 31.792602-24.170492 36.226757-55.383466 9.332013-109.723601 24.75012-164.527439 37.588882a53.035972 53.035972 0 0 1-13.911075 1.825829c-134.270852-5.071746-268.541703-10.346362-402.841536-15.447089-155.746073-5.912207-311.521128-11.447655-467.2672-17.53375-192.291625-7.535165-384.554269-15.447089-576.816914-23.243088a82.394136 82.394136 0 0 1-18.98282-2.811196c99.435202-3.91249 198.899386-7.680072 298.334588-11.737469 224.837744-9.187106 449.704469-18.5481 674.542212-27.764187 157.311069-6.433872 314.622138-12.896725 471.933207-18.895876 13.244502-0.492684 26.865763 1.507033 39.936377 4.11536 60.745026 12.085246 121.316163 24.808083 183.771092 37.675827zM10937.118728 506.710893c-89.813376 3.448787-179.626751 6.839612-269.440127 10.317381l-724.969858 27.938075c-157.398013 6.057114-314.796026 12.056265-472.19404 18.026434-3.970453 0.144907-8.143775 0.840461-11.853395-0.115926-63.672148-16.142643-127.286333-32.517137-193.334956-49.471259v-25.35873c68.598987-14.519684 134.792517-34.458891 202.29021-41.066651 60.397249-5.912207 122.243568 2.782215 183.452297 5.187671 142.298701 5.651374 284.597402 11.302748 426.867122 17.128011 225.736167 9.245068 451.472335 18.664025 677.208501 27.909093 60.6291 2.492401 121.287182 4.608043 181.916283 6.926556l0.057963 2.579345zM6834.887725 657.327258c-79.409051 0.434721-140.762686-58.745309-141.400277-136.473439-0.637591-77.844055 62.252059-142.095831 139.458523-142.472589 78.220813-0.347777 144.037585 64.454646 143.950641 141.777036-0.086944 75.87332-63.09252 136.70529-142.008887 137.168992zM4330.836329 521.317522c-0.60861 77.293408-62.831687 136.966122-141.777036 135.980754-79.524977-0.985368-141.081482-61.23771-140.704724-137.74862 0.40574-78.220813 65.555939-142.327682 143.602865-141.313333 77.409334 1.014349 139.487505 64.94733 138.878895 143.081199zM5124.202304 91.030595c63.29539 3.622676 128.213738 12.548949 188.755894 41.588316 33.589449 16.113661 61.759375 38.690176 80.568307 71.699998 40.602949 71.265276 6.839612 166.005491-68.164266 190.668666-5.129709 1.680922-10.665157 2.173605-16.171624 3.245918 5.390541-22.576515 13.82413-44.051736 15.099312-65.961679 4.694988-79.814791-35.560185-138.762969-96.247247-183.655167-31.937509-23.590864-69.816206-39.066935-103.840376-57.586052zM5692.585628 616.782272c-38.13953 106.883423-3.361843 201.217898 97.580392 264.339399 25.735488 16.08468 54.398098 27.474372 85.987831 43.153313-83.640336-6.346928-162.093001-15.591996-228.228569-65.874735-69.729262-53.006991-80.394419-142.878329-25.387711-205.014462 18.200323-20.489854 40.458042-34.342965 70.048057-36.603515zM5592.078114 308.970764c120.012 30.662327 220.490533-23.156143 271.063085-144.182492 9.07118-21.678091 15.012368-44.660346 23.590865-66.80214-0.231851 77.467297-2.927122 154.731724-42.486741 224.692837-42.196926 74.598138-122.359494 99.232332-193.363937 60.918914-29.503071-15.88181-49.268389-39.443693-58.803272-74.627119zM9208.609742 499.349617c-0.376758 48.775705-43.211276 91.030595-92.015963 90.798743-50.021906-0.260833-91.088557-41.24054-91.262446-91.14652-0.20287-50.369683 42.718592-93.00133 92.798461-92.247814 48.920612 0.753517 90.856706 43.674978 90.479948 92.595591zM1998.992443 499.00184c0.086944 49.761073-40.979707 90.856706-90.972631 91.088557-49.876999 0.231851-91.34939-40.747856-91.610223-90.537911-0.289814-50.543571 42.167945-93.262163 92.247813-92.79846 48.978575 0.434721 90.248097 42.573685 90.335041 92.247814zM5109.218917 915.174822c-0.695554-79.264144 5.071746-156.238757 46.486175-225.417371 48.138115-80.481363 143.602864-101.174087 209.361673-44.863216 17.185973 14.722554 28.372796 36.429627 42.921461 55.760224-36.719441-1.709903-69.091671-9.650808-98.420853-3.419806-104.362041 22.170775-159.716526 96.30521-190.639685 192.871254-2.405457 7.535165-3.825546 15.389126-5.825263 23.069198-0.144907 0.463702-1.304163 0.666572-3.883508 1.999717z"
                fill="#F39801" p-id="6415"></path>
              <path
                d="M5528.463929 482.91716c190.958481 3.593694 353.167407 182.843687 375.251238 400.320154-17.417825-40.689893-36.429627-96.479099-64.164832-147.515354-50.166813-92.247814-124.504118-157.716809-229.619675-182.553874-12.346079-2.927122-25.329748-7.390258-37.443976-6.057113-27.387428 3.072029-36.052868-10.92599-38.226474-34.458891-0.869442-9.332013-3.535731-18.490137-5.796281-29.734922zM5471.602411 533.22888c-209.158803-9.07118-355.949622-200.580307-379.946226-431.098407 22.373645 87.234031 51.297088 165.976509 104.854725 233.242351 62.339003 78.278776 140.762686 127.547166 242.980104 134.125945 6.404891 0.40574 15.302182 7.593128 17.794583 13.737186 6.231002 15.331164 9.360994 31.879546 14.316814 49.992925zM5526.116435 534.706931c10.346362 199.073274-168.179096 363.455806-368.469589 402.986443 38.835083-20.258002 91.291427-42.805536 138.618062-73.322955 85.176351-54.977726 144.675176-130.706139 164.005774-233.068463 3.361843-17.852546 6.057114-36.661478 3.970452-54.456061-2.202587-18.808932 4.781932-25.706507 21.098464-29.561034 13.650242-3.187955 26.865763-8.201738 40.776837-12.57793zM5474.616478 479.990038c-29.590015-160.470042 170.32372-378.410211 367.803017-401.914132-34.63278 16.171624-68.685931 29.937792-100.652422 47.471543-93.030312 50.978292-164.933179 121.634959-196.52291 225.823111-8.172756 26.981689-11.418674 56.108001-12.346079 84.393853-0.637591 19.301616-5.622393 29.416127-24.634195 33.241672-11.389692 2.26055-22.257719 7.158407-33.647411 10.983953z"
                fill="#F39801" p-id="6416"></path>
            </svg>
          </div>
          <button class="quote" @click="flushQuote()">
            <div :class="{ 'rotated': isRotated, 'rotate-initial': !isRotated }" @click="rotateSvg">
              <RefreshCcw size="20px" color="#d3b573" />
            </div>
          </button>
        </div>
        <!-- 菜单区 -->
        <div class="menu-title"> -文字织梦，心随笔动- </div>
        <button class="value" :class="{ 'active': activePath === '/article' }" @click="goTo('/article')">
          <Newspaper size="16px" />
          文章
        </button>
        <button class="value" :class="{ 'active': activePath === '/moment' }" @click="goTo('/moment')">
          <Camera size="16px" />
          瞬间
        </button>
        <button class="value" :class="{ 'active': activePath === '/todo' }" @click="goTo('/todo')">
          <square-check-big size="16px" />
          TODO
        </button>
        <div class="menu-title">-他山之石，可以攻玉-</div>
        <button class="value" :class="{ 'active': activePath === '/third/douban' }" @click="goTo('/third/douban')">
          <svg t="1741529655996" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
            p-id="21642" id="mx_n_1741529655996" width="20" height="20">
            <path
              d="M851.665455 1021.998545H170.333091A170.356364 170.356364 0 0 1 0 851.665455V170.333091A170.356364 170.356364 0 0 1 170.356364 0h681.309091a170.333091 170.333091 0 0 1 170.356363 170.356364v681.309091a170.333091 170.333091 0 0 1-170.356363 170.356363z"
              fill="#138717" p-id="21643"></path>
            <path
              d="M295.726545 573.602909v-208.593454h445.533091v208.593454H295.749818zM232.727273 767.697455v-54.202182h137.378909l-32.116364-141.172364h76.846546l34.676363 141.172364h136.727273l34.676364-141.172364h76.869818l-32.768 141.172364h138.007273v54.178909H232.727273z m141.800727-248.296728h287.976727v-100.817454H374.504727v100.817454z m-124.16-209.221818V256h535.621818v54.178909H250.368z"
              fill="#FFFFFF" p-id="21644"></path>
          </svg>
          豆瓣
        </button>
        <button class="value" :class="{ 'active': activePath === '/third/weread' }" @click="goTo('/third/weread')">
          <svg t="1741529630027" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
            p-id="19549" id="mx_n_1741529630028" width="20" height="20">
            <path
              d="M204.078 0h615.845q202.07 0 202.07 202.07v615.845q0 202.07-202.07 202.07H204.077q-202.07 0-202.07-202.07V202.069Q2.008 0 204.078 0z"
              fill="#4496D3" p-id="19550"></path>
            <path
              d="M616.087 869.276a106.657 106.657 0 0 0-102.641 77.663 106.657 106.657 0 0 0-102.641-77.663H7.63A202.11 202.11 0 0 0 204.077 1024h615.846a202.11 202.11 0 0 0 196.447-154.724z m255.437-128.14c-44.654 44.172-99.026 54.934-157.816 35.217-19.356-6.506-35.258-8.032-52.204 3.212a73.326 73.326 0 0 1-11.324 3.775c15.46-26.865 4.015-43.65-9.036-62.685-28.993-42.285-23.09-96.738 11.405-136.051 56.22-64.251 166.731-64.251 223.112 0 40.96 46.662 40.076 112.64-4.137 156.531z"
              fill="#FFFFFF" p-id="19551"></path>
            <path
              d="M818.96 611.187a20.078 20.078 0 0 0-20.883 19.276 19.516 19.516 0 0 0 18.473 21.444 20.078 20.078 0 0 0 22.006-18.03 20.68 20.68 0 0 0-19.597-22.69z m-108.906 0a20.078 20.078 0 0 0-20.079 22.207 19.556 19.556 0 0 0 21.404 18.472 20.078 20.078 0 0 0 19.275-20.921 20.922 20.922 0 0 0-20.6-19.758z"
              fill="#4496D3" p-id="19552"></path>
          </svg>
          微信读书
        </button>
        <div class="menu-title">-时光流转，岁月长歌-</div>
        <button class="value" :class="{ 'active': activePath === '/analyse/index' }" @click="goTo('/analyse/index')">
          <svg t="1741529828911" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
            p-id="23816" width="20" height="20">
            <path d="M782.848 641.536m-185.856 0a185.856 185.856 0 1 0 371.712 0 185.856 185.856 0 1 0-371.712 0Z"
              fill="#d4d0f3" p-id="23817"></path>
            <path
              d="M293.376 257.024h-66.56c-16.896 0-30.72-13.824-30.72-30.72s13.824-30.72 30.72-30.72h66.56c16.896 0 30.72 13.824 30.72 30.72s-13.824 30.72-30.72 30.72z"
              fill="#d4d0f3" p-id="23818"></path>
            <path
              d="M861.184 156.16v534.016H158.72V156.16h702.464m24.064-61.44H134.144c-20.48 0-37.376 16.896-37.376 37.376v582.656c0 20.48 16.896 37.376 37.376 37.376h751.104c20.48 0 37.376-16.896 37.376-37.376V132.096c0-20.48-16.896-37.376-37.376-37.376z"
              fill="#d4d0f3" p-id="23819"></path>
            <path
              d="M509.44 645.12c-6.656 0-12.8-2.048-17.92-6.144l-76.8-56.32c-4.608-3.584-8.704-8.192-10.752-13.824l-49.664-131.584L332.8 563.2c-2.56 14.848-15.36 25.6-30.208 25.6H240.64c-16.896 0-30.72-13.824-30.72-30.72s13.824-30.72 30.72-30.72h35.84l35.84-212.48c2.56-13.824 13.312-24.064 27.136-25.6 13.824-1.536 26.624 6.656 31.744 19.968l86.528 229.376 38.4 28.16 37.888-88.576c4.608-10.752 14.848-17.92 26.624-18.432 11.776-0.512 22.528 5.12 28.672 15.36l23.04 39.936 62.976-218.624c4.096-13.824 16.384-23.04 30.72-22.016 14.336 0.512 26.112 10.752 28.672 25.088l39.936 208.384h7.168c16.896 0 30.72 13.824 30.72 30.72s-13.824 30.72-30.72 30.72h-32.256c-14.848 0-27.136-10.24-30.208-25.088l-20.48-107.008-47.104 164.864c-3.584 11.776-13.312 20.48-25.6 22.016-12.288 1.536-24.064-4.608-30.208-15.36l-28.16-49.152-29.184 67.584c-3.584 8.704-11.264 14.848-19.968 17.408-3.584 0-6.656 0.512-9.216 0.512zM558.08 914.944H128c-16.896 0-30.72-13.824-30.72-30.72s13.824-30.72 30.72-30.72h430.08c16.896 0 30.72 13.824 30.72 30.72s-13.824 30.72-30.72 30.72zM745.472 914.944h-96.256c-16.896 0-30.72-13.824-30.72-30.72s13.824-30.72 30.72-30.72h96.256c16.896 0 30.72 13.824 30.72 30.72s-13.312 30.72-30.72 30.72zM892.928 914.944h-50.176c-16.896 0-30.72-13.824-30.72-30.72s13.824-30.72 30.72-30.72h50.176c16.896 0 30.72 13.824 30.72 30.72s-13.824 30.72-30.72 30.72z"
              fill="#d4d0f3" p-id="23820"></path>
          </svg>
          数据一览
        </button>
        <div class="footer">
          <span style=" cursor: pointer;" @click="goTo('/indexPage')">
            <House color="#F5F5F4" />
          </span> 
          <EllipsisVertical size="29px" color="#4E4E51" />
          <span style=" cursor: pointer;" @click="goTo('/settings')">
            <Settings color="#F5F5F4" />
          </span>
        </div>

      </div>
      <div style="flex: 1;">
        <router-view @scrollToTop="scrollToTop" />
      </div>
    </div>
  </div>

</template>
<script setup>
import { useRouter, useRoute } from 'vue-router';
import { ref, watch, nextTick,onMounted  } from 'vue';
import SevenSegmentClock from './index/SevenSegmentClock.vue';
import { SquareCheckBig, Camera, Newspaper, RefreshCcw, EllipsisVertical, Settings, House } from 'lucide-vue-next';
import {getQuote} from '@/js/index/indexPage.js';

const contentLayer = ref(null);
let quote_content = ref('');
const flushQuote=()=>{
  getQuote().then((content) => {
    quote_content.value = content;
  });
}
 
const scrollToTop = () => {
  nextTick(() => {
    contentLayer.value.scroll({ top: 0, behavior: 'smooth' });
  });
};
onMounted(() => {
  flushQuote()
});
const router = useRouter();
const route = useRoute();
const activePath = ref(route.path.replace('/', '') || 'default');
const backgroundImage = ref('');
backgroundImage.value = `${require('@/assets/pngs/sky.png')}`;
const goTo = (path) => {
  router.push(path);
  activePath.value = path.replace('/', '');
};

watch(() => route.path, (newPath) => {
  activePath.value = newPath;
  console.log(newPath);
  switch (true) {
    case newPath === '/article':
      backgroundImage.value = `${require('@/assets/pngs/article.png')}`;
      break;
    case newPath === '/moment':
      backgroundImage.value = `${require('@/assets/pngs/moment.png')}`;
      break;
    case newPath === '/todo':
      backgroundImage.value = `${require('@/assets/pngs/todo.png')}`;
      break;
    case newPath.startsWith('/articleDetail'):
      backgroundImage.value = `${require('@/assets/pngs/article-detail.png')}`;
      break;
    case newPath === '/third/douban':
      backgroundImage.value = `${require('@/assets/pngs/douban.png')}`;
      break;
    case newPath === '/third/weread':
      backgroundImage.value = `${require('@/assets/pngs/weread.png')}`;
      break;
    case newPath === '/writeArticle':
      backgroundImage.value = `${require('@/assets/pngs/write-article.png')}`;
      break;
    case newPath === '/analyse/article':
      backgroundImage.value = `${require('@/assets/pngs/ana_article-back.png')}`;
      break;
    case newPath === '/analyse/todo':
      backgroundImage.value = `${require('@/assets/pngs/ana_todo-back.png')}`;
      break;
    case newPath === '/analyse/douban':
      backgroundImage.value = `${require('@/assets/pngs/ana_douban-back.png')}`;
      break;
      case newPath === '/analyse/weread':
      backgroundImage.value = `${require('@/assets/pngs/ana_weread-back.png')}`;
      break;
    case newPath === '/settings':
      backgroundImage.value = `${require('@/assets/pngs/settings1.png')}`;
      break;
    default:
      backgroundImage.value = `${require('@/assets/pngs/sky.png')}`;
      break;
  }
});

const isRotated = ref(false);

const rotateSvg = () => {
  console.log("点击之后，在这里更新名言```");

  isRotated.value = !isRotated.value;
};
</script>