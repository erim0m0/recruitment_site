<template>
    <div class="CoProfileUpdate">
        <!-- top header wrapper start -->
        <div class="page_title_section">

            <div class="page_header">
                <div class="container">
                    <div class="row">
                        <!-- section_heading start -->
                        <div class="col-xl-9 col-lg-7 col-md-7 col-12 col-sm-12">
                            <h1>ویرایش پروفایل کارفرما</h1>
                        </div>
                        <div class="col-xl-3 col-lg-5 col-md-5 col-12 col-sm-12">
                            <div class="sub_title_section">
                                <ul class="sub_title">
                                    <li> <a href="#"> خانه </a>&nbsp; / &nbsp; </li>
                                    <li>ویرایش پروفایل</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- top header wrapper end -->
        <!--employee dashboard wrapper start-->
        <div class="employe_dashboard_wrapper jb_cover">
            <div class="container">

                <div class="row">
                    <div class="col-lg-3 col-md-12 col-sm-12 col-12">
                        <div class="emp_dashboard_sidebar jb_cover">
                            <div class="emp_web_profile jb_cover">
                                <img class="logo-img" :src="logo" alt="logo-img" />
                                <h4>فن آوری وب استروت</h4>
                                <p>@Webstrot</p>
                                <div class="skills jb_cover">
                                    <div class="skill-item jb_cover">
                                        <h6>پروفایل<span>70%</span></h6>
                                        <div class="skills-progress"><span data-value="70%"></span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="emp_follow_link jb_cover">
                                <ul class="feedlist">
                                    <li><a href="comp_employer_dashboard.html"><i class="fas fa-tachometer-alt"></i> داشبورد
                                        </a></li>
                                    <li>
                                        <a href="comp_employer_edit_profile.html" class="link_active"> <i
                                                class="fas fa-edit"></i>ویرایش پروفایل
                                        </a>
                                    </li>
                                    <li><a href="comp_company_page.html"><i class="fas fa-file"></i>صفحه شرکت </a></li>
                                    <li><a href="comp_employer_manage_jobs.html"><i class="fas fa-suitcase"></i>مدیریت
                                            مشاغل</a></li>
                                    <li><a href="comp_applications.html"><i class="fas fa-mobile"></i>برنامه ها</a></li>
                                    <li><a href="comp_post_new_job.html"><i class="fas fa-user-plus"></i>ارسال شغل جدید</a>
                                    </li>
                                    <li><a href="message.html"><i class="fas fa-envelope"></i>پیام</a></li>
                                    <li><a href="pricing_plans.html"><i class="fas fa-tag"></i>طرح های قیمت گذاری</a></li>
                                </ul>
                                <ul class="feedlist logout_link jb_cover">
                                    <li><a href="#"><i class="fas fa-power-off"></i> خروج </a></li>
                                    <li>
                                        <a href="#" data-toggle="modal" data-target="#myModal"><i
                                                class="fas fa-trash-alt"></i>حذف پروفایل
                                        </a>
                                    </li>

                                </ul>
                            </div>
                        </div>
                        <div class="modal fade delete_popup" id="myModal" role="dialog">
                            <div class="modal-dialog">
                                <div class="modal-content">
                                    <button type="button" class="close" data-dismiss="modal">&times;</button>
                                    <div class="row">
                                        <div class="col-lg-12 col-md-12 col-sm-12 col-12">

                                            <div class="delett_cntn jb_cover">
                                                <h1><i class="fas fa-trash-alt"></i> حذف حساب</h1>
                                                <p>شما مطمئن هستید! شما میخواهید پروفایل خود را حذف کنید.
                                                    <br> نمی تواند برگردانده شود!
                                                </p>

                                                <div class="delete_jb_form">

                                                    <!-- <input type="password" name="password"
                                                        placeholder="رمز عبور را وارد کنید"> -->
                                                </div>
                                                <div class="header_btn search_btn applt_pop_btn">

                                                    <a href="#">ذخیره به روزرسانی</a>

                                                </div>
                                                <div class="cancel_wrapper">
                                                    <a href="#" class="" data-dismiss="modal">لغو</a>
                                                </div>
                                                <div class="login_remember_box jb_cover">
                                                    <label class="control control--checkbox">شما شرایط و ضوابط <a href="#">و
                                                            حریم خصوصی </a> ما را <a href="#">میپذیرید</a>
                                                        <input type="checkbox">
                                                        <span class="control__indicator"></span>
                                                    </label>
                                                </div>
                                            </div>

                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-9 col-md-12 col-sm-12 col-12">
                        <div class="row">
                            <form @submit.prevent="createCoProfile">
                                <div class="col-lg-12 col-md-12 col-sm-12 col-12">
                                    <div class="job_listing_left_fullwidth jb_cover">
                                        <div class="row">
                                            <div class="input-group">
                                                <h5 class="ml-3">آپلود لوگو</h5>
                                                <div>
                                                    <input type="file" ref="file">
                                                    <div class="invalid-feedback" :class="{
                                                        'd-block': logoE === true
                                                    }" v-if="logoE">
                                                        {{ logoEM }}
                                                    </div>
                                                    <button @click="uploadLogoFile" type="button">Upload</button>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="browse_img_banner jb_cover">
                                        <div class="jp_job_post_side_img">
                                            <img :src="companyView" alt="post_img">
                                        </div>
                                        <h5 class="ml-3">آپلود نمایی از شرکت</h5>
                                        <div>
                                            <input type="file" ref="coViewFile">
                                        </div>
                                    </div>
                                    <div class="browse_img_banner jb_cover">

                                        <div class="row">
                                            <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                                <div class="contect_form3">
                                                    <label>نام شرکت*</label>
                                                    <input v-model="name" type="text">
                                                    <div class="invalid-feedback" :class="{
                                                        'd-block': nameE === true
                                                    }" v-if="nameE">
                                                        {{ nameEM }}
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                                <div class="contect_form3">
                                                    <label>نام شرکت (به انگلیسی) *</label>
                                                    <input v-model="englishName" type="text">
                                                    <div class="invalid-feedback" :class="{
                                                        'd-block': englishNameE === true
                                                    }" v-if="englishNameE">
                                                        {{ englishNameEM }}
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                                <div class="contect_form3">
                                                    <label>سایت شرکت</label>
                                                    <input v-model="websiteAddr" type="text">
                                                </div>
                                            </div>
                                            <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                                <div class="contect_form3">
                                                    <label>ایمیل*</label>
                                                    <input v-model="email" type="email">
                                                    <div class="invalid-feedback" :class="{
                                                        'd-block': emailE === true
                                                    }" v-if="emailE">
                                                        {{ emailEM }}
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                                <div class="contect_form3">
                                                    <label>شماره تلفن*</label>
                                                    <input v-model="telephone" type="number">
                                                    <div class="invalid-feedback" :class="{
                                                        'd-block': telephoneE === true
                                                    }" v-if="telephoneE">
                                                        {{ telephoneEM }}
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                                <div class="contect_form3">
                                                    <label>نوع صنعت*</label>
                                                    <select v-model="industry">
                                                        <option value="2">فناوری</option>
                                                        <option value="3">مراقبت های بهداشتی</option>
                                                        <option value="دارایی، مالی، سرمایه گذاری">دارایی، مالی، سرمایه
                                                            گذاری</option>
                                                        <option value="خرده فروشی">خرده فروشی</option>
                                                        <option value="انرژی">انرژی</option>
                                                        <option value="تولید">تولید</option>
                                                        <option value="حمل و نقل و تدارکات">حمل و نقل و تدارکات
                                                        </option>
                                                        <option value="رسانه و سرگرمی">رسانه و سرگرمی</option>
                                                        <option value="تحصیلات">تحصیلات</option>
                                                        <option value="مهمان نوازی و گردشگری">مهمان نوازی و گردشگری</option>
                                                    </select>
                                                    <div class="invalid-feedback" :class="{
                                                        'd-block': industryE === true
                                                    }" v-if="industryE">
                                                        {{ industryEM }}
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                                <div class="select_box">
                                                    <label>کشور</label>
                                                    <select v-model="country">
                                                        <option value="ایران">ایران</option>
                                                    </select>
                                                </div>
                                            </div>
                                            <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                                <div class="select_box">
                                                    <label>استان*</label>
                                                    <select id="province" :value="province" v-model="province">
                                                        <option v-for="province in provinceList" :value="province.id">
                                                            {{ province.name }}
                                                        </option>
                                                    </select>
                                                    <div class="invalid-feedback" :class="{
                                                        'd-block': provinceE === true
                                                    }" v-if="provinceE">
                                                        {{ provinceEM }}
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                                <div class="select_box">
                                                    <label>شهر*</label>
                                                    <select v-model="city" :value="city">
                                                        <option v-for="city in cityList" :value="city.name">
                                                            {{ city.name }}
                                                        </option>
                                                    </select>
                                                    <div class="invalid-feedback" :class="{
                                                        'd-block': cityE === true
                                                    }" v-if="cityE">
                                                        {{ cityEM }}
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                                <div class="contect_form3">
                                                    <label>سال تأسیس*</label>
                                                    <select v-model="establishedYear">
                                                        <option v-for="i in 40" :value="i + 1359">{{ i + 1359 }}</option>
                                                        <option value="1400">1400</option>
                                                        <option value="1401">1401</option>
                                                    </select>
                                                    <div class="invalid-feedback" :class="{
                                                        'd-block': establishedYearE === true
                                                    }" v-if="establishedYearE">
                                                        {{ establishedYearEM }}
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                                <div class="select_box">
                                                    <label>نوع مالکیت*</label>
                                                    <select v-model="typeOfOwnership">
                                                        <option value="private">خصوصی</option>
                                                        <option value="governmental">دولتی</option>
                                                        <option value="other">غیره ( وقفی و ...)</option>
                                                    </select>
                                                    <div class="invalid-feedback" :class="{
                                                        'd-block': typeOfOwnershipE === true
                                                    }" v-if="typeOfOwnershipE">
                                                        {{ typeOfOwnershipEM }}
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-lg-12 col-md-12 col-sm-12 col-12">
                                            <div class="job_filter_category_sidebar jb_cover">
                                                <div class="job_filter_sidebar_heading jb_cover">
                                                    <h1>درباره ی شرکت</h1>
                                                </div>
                                                <div class="job_overview_header jb_cover">
                                                    <div class="row">
                                                        <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                                            <div class="contect_form3">
                                                                <textarea v-model="companyDescription" rows="3"
                                                                    cols="85"></textarea>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <button type="submit">ذخیره تغییرات</button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!--employee dashboard wrapper end-->
    </div>
</template>

<script>
import axios from 'axios'
import provinceData from '@/assets/cities_and_provinces/provinces.json'
import cityData from '@/assets/cities_and_provinces/cities.json'
import '@/assets/dashboard/css/font-awesome.css'
import '@/assets/dashboard/css/nice-select.css'
import '@/assets/dashboard/css/reset.css'
import '@/assets/dashboard/css/style.css'
import '@/assets/dashboard/css/responsive.css'

export default {
    name: 'CoProfileUpdate',
    data() {
        return {
            created: false,
            provinceList: provinceData,
            cityList: [],
            name: "",
            nameE: false,
            nameEM: false,
            englishName: "",
            englishNameE: false,
            englishNameEM: false,
            email: "",
            emailE: false,
            emailEM: false,
            websiteAddr: "",
            websiteAddrE: false,
            websiteAddrEM: false,
            telephone: "",
            telephoneE: false,
            telephoneEM: false,
            industry: "",
            industryE: false,
            industryEM: false,
            country: "",
            countryE: false,
            countryEM: false,
            province: "",
            provinceE: false,
            provinceEM: false,
            city: "",
            cityE: false,
            cityEM: false,
            logo: "",
            logoE: false,
            logoEM: false,
            companyDescription: "",
            companyDescriptionE: false,
            companyDescriptionEM: false,
            companyView: "",
            companyViewE: false,
            companyViewEM: false,
            establishedYear: "",
            establishedYearE: false,
            establishedYearEM: false,
            typeOfOwnership: "",
            typeOfOwnershipE: false,
            typeOfOwnershipEM: false,
            operator: "",
            operatorE: false,
            operatorEM: false,
            createdAt: "",
            createdAtE: false,
            createdAtEM: false,
            numberOfAd: "",
            numberOfAdE: false,
            numberOfAdEM: false,
        }
    },
    methods: {
        uploadLogoFile() {
            let access = true
            const companyName = localStorage.getItem("companyName");
            const formData = new FormData();
            formData.append('logo', this.$refs.file.files[0]);

            if (!this.$refs.file.files[0]) {
                this.logoE = true
                this.logoEM = "لطفا عکس مورد نظر را آپلود کنید."
                access = false
            }

            if (access) {
                axios
                    .patch(`/account/api/company/profile/update/iranable/`, formData, {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        }
                    })
                    .then(response => {
                        this.logo = response.data.logo
                    })
                    .catch(error => {
                        if (error.response.status == 404) {
                            this.logoE = true
                            this.logoEM = "ابتدا فرم پایین را تکمیل کنید."
                        }
                    });
            }
        },
        createCoProfile() {
            let access = true

            const isEnglish = /^[a-zA-Z0-9\s]+$/.test(this.englishName);
            if (!isEnglish) {
                this.englishNameE = true
                this.englishNameEM = "لطفا به زبان انگلیسی وارد کنید."
                access = false
            } else {
                this.englishNameE = false
            }

            if (this.name === "") {
                this.nameE = true
                this.nameEM = "الزامی است"
            } else {
                this.nameE = false
            }

            if (this.englishName === "") {
                this.englishNameE = true
                this.englishNameEM = "الزامی است"
            } else {
                this.englishNameE = false
            }

            if (this.province === "") {
                access = false
                this.provinceE = true
                this.provinceEM = "الزامی است"
            } else {
                this.provinceE = false
            }

            if (this.city === "") {
                access = false
                this.cityE = true
                this.cityEM = "الزامی است"
            } else {
                this.cityE = false
            }

            if (this.establishedYear === "") {
                access = false
                this.establishedYearE = true
                this.establishedYearEM = "الزامی است"
            } else {
                this.establishedYearE = false
            }

            if (this.typeOfOwnership === "") {
                access = false
                this.typeOfOwnershipE = true
                this.typeOfOwnershipEM = "الزامی است"
            } else {
                this.typeOfOwnershipE = false
            }

            if (this.telephone === "") {
                access = false
                this.telephoneE = true
                this.telephoneEM = "الزامی است"
            } else {
                this.telephoneE = false
            }

            if (this.email === "") {
                access = false
                this.emailE = true
                this.emailEM = "الزامی است"
            } else {
                this.emailE = false
            }

            if (!this.industry) {
                access = false
                this.industryE = true
                this.industryEM = "الزامی است"
            } else {
                this.industryE = false
            }

            if (access && !this.created) {
                let companyData = {
                    "name": this.name,
                    "english_name": this.englishName,
                    "email": this.email,
                    "website_addr": this.websiteAddr,
                    "telephone": this.telephone,
                    "industry": this.industry,
                    "country": this.country,
                    "province": provinceData.find(province => province.id == this.province).name,
                    "city": this.city,
                    "company_description": this.companyDescription,
                    "established_year": this.establishedYear,
                    "type_of_ownership": this.typeOfOwnership
                }
                const formData = new FormData();

                if (this.$refs.coViewFile.files[0]) {
                    formData.append('company_view', this.$refs.coViewFile.files[0]);
                }

                for (let key in companyData) {
                    formData.append(key, companyData[key]);
                }

                axios
                    .post(`/account/api/company/profile/`, formData, {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        }
                    })
                    .then(response => {
                        const getData = response.data
                        const getProvince = provinceData.find(province => province.name == getData.province);

                        this.created = true

                        this.name = getData.name
                        this.englishName = getData.english_name
                        this.email = getData.email
                        this.websiteAddr = getData.website_addr
                        this.telephone = getData.telephone
                        this.industry = getData.industry
                        this.country = getData.country
                        this.province = getProvince.id
                        this.city = getData.city
                        this.logo = getData.logo
                        this.companyDescription = getData.company_description
                        this.companyView = getData.company_view
                        this.establishedYear = getData.established_year
                        this.typeOfOwnership = getData.type_of_ownership

                        localStorage.setItem("companyName", getData.english_name);
                    })
                    .catch(e => {
                        console.log(e.response);
                    })

            } else if (access && this.created) {
                const companyName = localStorage.getItem("companyName");
                let companyData = {
                    "name": this.name,
                    "english_name": this.englishName,
                    "email": this.email,
                    "website_addr": this.websiteAddr,
                    "telephone": this.telephone,
                    "industry": this.industry,
                    "country": this.country,
                    "province": provinceData.find(province => province.id == this.province).name,
                    "city": this.city,
                    "company_description": this.companyDescription,
                    "established_year": this.establishedYear,
                    "type_of_ownership": this.typeOfOwnership
                }

                const formData = new FormData();

                if (this.$refs.coViewFile.files[0]) {
                    formData.append('company_view', this.$refs.coViewFile.files[0]);
                }

                for (let key in companyData) {
                    formData.append(key, companyData[key]);
                }

                axios
                    .patch(`/account/api/company/profile/update/${companyName}/`, formData, {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        }
                    })
                    .then(response => {
                        const getData = response.data
                        const getProvince = provinceData.find(province => province.name == getData.province);

                        this.name = getData.name
                        this.englishName = getData.english_name
                        this.email = getData.email
                        this.websiteAddr = getData.website_addr
                        this.telephone = getData.telephone
                        this.industry = getData.industry
                        this.country = getData.country
                        this.province = getProvince.id
                        this.city = getData.city
                        this.logo = getData.logo
                        this.companyDescription = getData.company_description
                        this.companyView = getData.company_view
                        this.establishedYear = getData.established_year
                        this.typeOfOwnership = getData.type_of_ownership
                    })
                    .catch(e => {
                        console.log(e.response);
                    })
            }
        },
    },
    watch: {
        province() {
            let provinceValue = this.province
            this.cityList = cityData.filter(item => item.province_id == provinceValue)
        },
    },
    mounted() {
        const companyName = localStorage.getItem("companyName");

        axios
            .get(`/account/api/company/profile/${companyName}/`)
            .then(response => {
                const getData = response.data
                const getProvince = provinceData.find(province => province.name === getData.province);
                this.cityList = cityData.filter(item => item.province_id == getProvince.name)

                this.created = true

                this.name = getData.name
                this.englishName = getData.english_name
                this.email = getData.email
                this.websiteAddr = getData.website_addr
                this.telephone = getData.telephone
                this.industry = getData.industry
                this.country = getData.country
                this.province = getProvince.id
                this.city = getData.city
                this.logo = getData.logo
                this.companyDescription = getData.company_description
                this.companyView = getData.company_view
                this.establishedYear = getData.established_year
                this.typeOfOwnership = getData.type_of_ownership
            })
            .catch(e => {
                console.log(e.response);
            })
    },
}


</script>

<style scoped>
.logo-img {
    width: 100%;
}

.wave-group {
    position: relative;
}

.wave-group .input {
    font-size: 16px;
    padding: 10px 10px 10px 5px;
    display: block;
    width: 200px;
    border: none;
    border-bottom: 1px solid #515151;
    background: transparent;
}

.wave-group .input:focus {
    outline: none;
}

.wave-group .label {
    color: #999;
    font-size: 18px;
    font-weight: normal;
    position: absolute;
    pointer-events: none;
    left: 5px;
    top: 10px;
    display: flex;
}

.wave-group .label-char {
    transition: 0.2s ease all;
    transition-delay: calc(var(--index) * .05s);
}

.wave-group .input:focus~label .label-char,
.wave-group .input:valid~label .label-char {
    transform: translateY(-20px);
    font-size: 14px;
    color: #5264AE;
}

.wave-group .bar {
    position: relative;
    display: block;
    width: 200px;
}

.wave-group .bar:before,
.wave-group .bar:after {
    content: '';
    height: 2px;
    width: 0;
    bottom: 1px;
    position: absolute;
    background: #5264AE;
    transition: 0.2s ease all;
    -moz-transition: 0.2s ease all;
    -webkit-transition: 0.2s ease all;
}

.wave-group .bar:before {
    left: 50%;
}

.wave-group .bar:after {
    right: 50%;
}

.wave-group .input:focus~.bar:before,
.wave-group .input:focus~.bar:after {
    width: 50%;
}

</style>

