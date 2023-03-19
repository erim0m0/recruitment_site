<template>
    <!-- top header wrapper start -->
    <div class="page_title_section">
        <div class="page_header">
            <div class="container">
                <div class="row">
                    <!-- section_heading start -->
                    <div class="col-xl-9 col-lg-7 col-md-7 col-12 col-sm-12">

                        <h1>ویرایش پروفایل داوطلب</h1>
                    </div>
                    <div class="col-xl-3 col-lg-5 col-md-5 col-12 col-sm-12">
                        <div class="sub_title_section">
                            <ul class="sub_title">
                                <li> <a href="#"> خانه </a>&nbsp; / &nbsp; </li>
                                <li>پروفایل داوطلب</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- top header wrapper end -->
    <!--employee dashboard wrapper start-->
    <div class="candidate_dashboard_wrapper jb_cover">
        <div class="container">

            <div class="row">
                <div class="col-lg-3 col-md-12 col-sm-12 col-12">
                    <div class="emp_dashboard_sidebar jb_cover">
                        <img :src="avatar" class="img-responsive" alt="post_img" />
                        <div class="emp_web_profile candidate_web_profile jb_cover">

                            <h4>آرش خادملو</h4>
                            <p>@username</p>
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
                                <li><a href="candidate_dashboard.html"><i class="fas fa-tachometer-alt"></i> داشبورد
                                    </a></li>
                                <li>
                                    <a href="candidate_edit_profile.html" class="link_active"> <i
                                            class="fas fa-edit"></i>ویرایش پروفایل
                                    </a>
                                </li>
                                <li><a href="candidate_resume.html"><i class="fas fa-file"></i>رزومه </a></li>
                                <li><a href="candidate_favourite_job.html"><i class="fas fa-heart"></i>موردعلاقه</a>
                                </li>
                                <li><a href="candidate_applied_job.html"><i class="fas fa-check-square"></i>شغل
                                        درخواستی</a></li>
                                <li><a href="message.html"><i class="fas fa-envelope"></i>پیام</a></li>

                                <li><a href="pricing_plans.html"><i class="fas fa-tag"></i>طرح های قیمت گذاری</a></li>
                            </ul>
                            <ul class="feedlist logout_link jb_cover">
                                <li><a href="#"><i class="fas fa-power-off"></i> خروج </a></li>
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

                                                <!-- <input type="password" name="password" placeholder="رمز عبور را وارد کنید"> -->
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
                        <form @submit.prevent="createProfile">
                            <div class="col-lg-12 col-md-12 col-sm-12 col-12">
                                <div class="job_listing_left_fullwidth jb_cover">
                                    <div class="row">
                                        <div class="col-lg-12 col-md-12 col-sm-12 col-12">
                                            <div class="jp_job_post_side_img">
                                                <img src="@/assets/images/pf1.jpg" alt="post_img">
                                            </div>
                                            <div class="jp_job_post_right_cont edit_profile_wrapper">
                                                <h4>JPEG یا PNG در اندازه 500x500px تصویر بند انگشتی</h4>

                                                <div class="width_50">
                                                    <input type="file" id="input-file-now-custom-233" class="dropify"
                                                        data-height="90" />
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <div class="browse_img_banner jb_cover">

                                    <div class="row">
                                        <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                            <div class="contect_form3">
                                                <label>نام*</label>
                                                <input v-model="firstName" type="text" placeholder="نام خود را وارد کنید.">
                                                <div class="invalid-feedback" :class="{
                                                    'd-block': firstNameE === true
                                                }" v-if="firstNameE">
                                                    {{ firstNameEM }}
                                                </div>
                                            </div>
                                        </div>
                                        <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                            <div class="contect_form3">
                                                <label>نام خانوادگی*</label>
                                                <input v-model="lastName" type="text"
                                                    placeholder="نام خانوادگی خود را وارد کنید.">
                                                <div class="invalid-feedback" :class="{
                                                    'd-block': lastNameE === true
                                                }" v-if="lastNameE">
                                                    {{ lastNameEM }}
                                                </div>
                                            </div>
                                        </div>
                                        <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                            <div class="contect_form3">
                                                <label>ایمیل</label>
                                                <input v-model="email" type="email" placeholder="ایمیل خود را وارد کنید.">
                                            </div>
                                        </div>
                                        <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                            <div class="contect_form3">
                                                <label>کد ملی*</label>
                                                <input v-model="nationalCode" type="text"
                                                    placeholder="کدملی خود را وارد کنید.">
                                                <div class="invalid-feedback" :class="{
                                                    'd-block': nationalCodeE === true
                                                }" v-if="nationalCodeE">
                                                    {{ nationalCodeEM }}
                                                </div>
                                            </div>
                                        </div>
                                        <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                            <div class="contect_form3">
                                                <label>آدرس</label>
                                                <input v-model="address" type="text">
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
                                                <label>استان</label>
                                                <select id="province" :value="province" v-model="province">
                                                    <option v-for="province in provinceList" :value="province.id">
                                                        {{ province.name }}
                                                    </option>
                                                </select>
                                            </div>
                                        </div>
                                        <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                            <div class="select_box">
                                                <label>شهر</label>
                                                <select v-model="city" :value="city">
                                                    <option v-for="city in cityList" :value="city.name">
                                                        {{ city.name }}
                                                    </option>
                                                </select>
                                            </div>
                                        </div>
                                        <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                            <div class="select_box">
                                                <label>متأهل هستید؟</label>
                                                <input v-model="isMarried" type="checkbox">
                                            </div>
                                        </div>
                                        <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                            <div class="select_box">
                                                <label>جنسیت‌</label>
                                                <select v-model="gender">
                                                    <option value="male">آقا</option>
                                                    <option value="female">خانم</option>
                                                </select>
                                            </div>
                                        </div>
                                    </div>
                                    <div>
                                        <div>
                                            <h5>تاریخ تولد*</h5>
                                        </div>
                                        <div class="row">
                                            <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                                <div class="contect_form3">
                                                    <label>روز</label>
                                                    <input v-model="dayOfBirth" type="number">
                                                    <div class="invalid-feedback" :class="{
                                                        'd-block': dayOfBirthE === true
                                                    }" v-if="dayOfBirthE">
                                                        {{ dayOfBirthEM }}
                                                    </div>
                                                </div>
                                                <div class="select_box">
                                                    <label>ماه</label>
                                                    <select v-model="monthOfBirth">
                                                        <option value="01" id="m01">فرودین</option>
                                                        <option value="02" id="m02">اردیبهشت</option>
                                                        <option value="03" id="m03">خرداد</option>
                                                        <option value="04" id="m04">تیر</option>
                                                        <option value="05" id="m05">مرداد</option>
                                                        <option value="06" id="m06">شهریور</option>
                                                        <option value="07" id="m07">مهر</option>
                                                        <option value="08" id="m08">آبان</option>
                                                        <option value="09" id="m09">آذر</option>
                                                        <option value="10" id="m10">دی</option>
                                                        <option value="11" id="m11">بهمن</option>
                                                        <option value="12" id="m12">اسفند</option>
                                                    </select>
                                                </div>
                                                <div class="contect_form3">
                                                    <label>سال</label>
                                                    <!-- <input v-model="yearOfBirth" type="number">
                                                    <div class="invalid-feedback" :class="{
                                                        'd-block': yearOfBirthE === true
                                                    }" v-if="yearOfBirthE">
                                                        {{ yearOfBirthEM }}
                                                    </div> -->
                                                    <select v-model="yearOfBirth">
                                                        <option v-for="i in 40" :value="i + 1359">{{ i + 1359 }}</option>
                                                        <option value="1400">1400</option>
                                                        <option value="1401">1401</option>
                                                    </select>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                        <div class="select_box">
                                            <label>وضعیت نظام وظیفه</label>
                                            <select v-model="militaryServiceStatus">
                                                <option value="دارای کارت پایان خدمت">دارای کارت پایان خدمت</option>
                                                <option value="در حال خدمت">در حال خدمت</option>
                                                <option value="معاف از رزم">معاف از رزم</option>
                                                <option value="معافیت تحصیلی">معافیت تحصیلی</option>
                                                <option value="معافیت پزشکی">معافیت پزشکی</option>
                                                <option value="سایر معافیت ها">سایر معافیت ها</option>
                                            </select>
                                        </div>
                                    </div>
                                    <div v-if="militaryServiceStatus === 'سایر معافیت ها'"
                                        class="col-lg-6 col-md-6 col-sm-12 col-12">
                                        <div class="select_box">
                                            <label>سایر معافیت ها</label>
                                            <input v-model="otherExemptions" type="text">
                                        </div>
                                    </div>
                                </div>

                                <div class="row">
                                    <div class="col-lg-12 col-md-12 col-sm-12 col-12">
                                        <div class="job_filter_category_sidebar jb_cover">
                                            <div class="job_filter_sidebar_heading jb_cover">
                                                <h1>درباره من</h1>
                                            </div>
                                            <div class="job_overview_header jb_cover">
                                                <div class="row">
                                                    <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                                        <div class="contect_form3">
                                                            <textarea v-model="aboutMe" rows="3" cols="85"></textarea>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <!-- <div class="row">
                                    <div class="col-lg-12 col-md-12 col-sm-12 col-12">
                                        <div class="job_filter_category_sidebar jb_cover">
                                            <div class="job_filter_sidebar_heading jb_cover">
                                                <h1>زبان های من</h1>
                                            </div>
                                            <div class="job_overview_header jb_cover">
                                                <div class="row">
                                                    <div id="languages" v-for="lng in language">
                                                        <h5 v-if="lng == 1">انگلیسی</h5>
                                                        <h5 v-if="lng == 2">فرانسوی</h5>
                                                        <h5 v-if="lng == 3">آلمانی</h5>
                                                    </div>
                                                    <div class="select_box">
                                                        <select :value="language">
                                                            <option value="1">انگلیسی</option>
                                                            <option value="2">فرانسوی</option>
                                                            <option value="3">آلمانی</option>
                                                        </select>
                                                    </div>
                                                    <div class="col-lg-12 col-md-12 col-sm-12 col-12">
                                                        <div class="header_btn search_btn jb_cover">
                                                            <a href="#">افزودن بیشتر</a>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div> -->
                                <div class="row">
                                    <div class="col-lg-12 col-md-12 col-sm-12 col-12">
                                        <div id="work-exp" class="job_filter_category_sidebar jb_cover">
                                            <div class="job_filter_sidebar_heading jb_cover">
                                                <h1>تجربه کاری</h1>
                                            </div>
                                            <div class="work-exp-container">
                                                <ul class="d-flex work-exp-title">
                                                    <li>شرکت</li>
                                                    <li>شغل</li>
                                                </ul>
                                                <ul class="d-flex work-exp-list" v-for="workExperience in workExperiences">
                                                    <li>{{ workExperience.company }}</li>
                                                    <li>{{ workExperience.job }}</li>
                                                </ul>
                                            </div>
                                            <div class="job_overview_header jb_cover">
                                                <div class="row">
                                                    <div class="contect_form3">
                                                        <label>شرکت</label>
                                                        <input v-model="company" type="text">
                                                        <div class="invalid-feedback" :class="{
                                                            'd-block': companyE === true
                                                        }" v-if="companyE">
                                                            {{ companyEM }}
                                                        </div>
                                                    </div>
                                                    <div class="contect_form3">
                                                        <label>شغل</label>
                                                        <input v-model="job" type="text">
                                                        <div class="invalid-feedback" :class="{
                                                            'd-block': jobE === true
                                                        }" v-if="jobE">
                                                            {{ jobEM }}
                                                        </div>
                                                    </div>
                                                    <button type="button" v-on:click="addWorkExperience">افزودن</button>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col-lg-12 col-md-12 col-sm-12 col-12">
                                        <div class="job_filter_category_sidebar jb_cover">
                                            <div class="job_filter_sidebar_heading jb_cover">
                                                <h1>مدرک تحصیلی</h1>
                                            </div>
                                            <div class="ed-record-container">
                                                <table>
                                                    <tr class="ed-record-title">
                                                        <th>رشته تحصیلی</th>
                                                        <th>مدرک تحصیلی</th>
                                                        <th>دانشگاه</th>
                                                        <th>معدل</th>
                                                    </tr>
                                                    <tr class="ed-record-list"
                                                        v-for="educationalRecord in educationalRecords">
                                                        <td>{{ educationalRecord.field_of_study }}</td>
                                                        <td>{{ educationalRecord.education }}</td>
                                                        <td>{{ educationalRecord.university }}</td>
                                                        <td>{{ educationalRecord.score }}</td>
                                                    </tr>
                                                </table>
                                            </div>
                                            <div class="job_overview_header jb_cover">
                                                <div class="row">
                                                    <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                                        <div class="contect_form3">
                                                            <label>رشته تحصیلی</label>
                                                            <input v-model="fieldOfStudy" type="text">
                                                            <div class="invalid-feedback" :class="{
                                                                'd-block': fieldOfStudyE === true
                                                            }" v-if="fieldOfStudyE">
                                                                {{ fieldOfStudyEM }}
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                                        <div class="contect_form3">
                                                            <label>مدرک تحصیلی</label>
                                                            <select v-bind:value="education" v-model="education">
                                                                <option value="DIPLOMA">دیپلم</option>
                                                                <option value="ASSOCIATE">فوق دیپلم</option>
                                                                <option value="BACHELOR">لیسانس</option>
                                                                <option value="MASTER">فوق لیسانس</option>
                                                                <option value="PHD">دکترا</option>
                                                                <option value="POSTDOC">فوق دکترا</option>
                                                            </select>
                                                            <div class="invalid-feedback" :class="{
                                                                'd-block': educationE === true
                                                            }" v-if="educationE">
                                                                {{ educationEM }}
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                                        <div class="contect_form3">
                                                            <label>دانشگاه</label>
                                                            <input v-model="university" type="text">
                                                            <div class="invalid-feedback" :class="{
                                                                'd-block': universityE === true
                                                            }" v-if="universityE">
                                                                {{ universityEM }}
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                                        <div class="contect_form3">
                                                            <label>معدل</label>
                                                            <input v-model="score" type="number">
                                                            <div class="invalid-feedback" :class="{
                                                                'd-block': scoreE === true
                                                            }" v-if="scoreE">
                                                                {{ scoreEM }}
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                                <button type="button" v-on:click="addEducationalRecord">افزودن</button>
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
    name: 'ProfileUpdate',
    data() {
        return {
            created: false,
            provinceList: provinceData,
            cityList: [],
            phone: "",
            phoneE: null,
            phoneEM: null,
            firstName: "",
            firstNameE: null,
            firstNameEM: null,
            lastName: "",
            lastNameE: null,
            lastNameEM: null,
            email: "",
            emailE: null,
            emailEM: null,
            avatar: "",
            avatarE: null,
            avatarEM: null,
            nationalCode: "",
            nationalCodeE: null,
            nationalCodeEM: null,
            passportNumber: "",
            passportNumberE: null,
            passportNumberEM: null,
            country: "",
            countryE: null,
            countryEM: null,
            province: "",
            provinceE: null,
            provinceEM: null,
            city: "",
            cityE: null,
            cityEM: null,
            address: "",
            addressE: null,
            addressEM: null,
            isMarried: "",
            isMarriedE: null,
            isMarriedEM: null,
            gender: "",
            genderE: null,
            genderEM: null,
            dayOfBirth: "",
            dayOfBirthE: null,
            dayOfBirthEM: null,
            monthOfBirth: "",
            monthOfBirthE: null,
            monthOfBirthEM: null,
            yearOfBirth: "",
            yearOfBirthE: null,
            yearOfBirthEM: null,
            militaryServiceStatus: "",
            militaryServiceStatusE: null,
            militaryServiceStatusEM: null,
            otherExemptions: "",
            otherExemptionsE: null,
            otherExemptionsEM: null,
            aboutMe: "",
            aboutMeE: null,
            aboutMeEM: null,
            language: "",
            languageE: null,
            languageEM: null,
            job: "",
            jobE: null,
            jobEM: null,
            company: "",
            companyE: null,
            companyEM: null,
            fieldOfStudy: "",
            fieldOfStudyE: null,
            fieldOfStudyEM: null,
            education: "",
            educationE: null,
            educationEM: null,
            university: "",
            universityE: null,
            universityEM: null,
            score: "",
            scoreE: null,
            scoreEM: null,
            workExperiences: [],
            educationalRecords: []
        }
    },
    methods: {
        addEducationalRecord() {
            let access = true

            if (this.fieldOfStudy === "") {
                this.fieldOfStudyE = true
                this.fieldOfStudyEM = "الزامی می باشد."
                access = false

            } else {
                this.fieldOfStudyE = false
            }

            if (this.education === "") {
                this.educationE = true
                this.educationEM = "الزامی می باشد."
                access = false
            } else {
                this.educationE = false
            }

            if (this.university === "") {
                this.universityE = true
                this.universityEM = "الزامی می باشد."
                access = false
            } else {
                this.universityE = false
            }

            if (this.score === "") {
                this.scoreE = true
                this.scoreEM = "الزامی می باشد."
                access = false
            } else {
                this.scoreE = false
            }

            if (access) {
                const newEdRecord = {
                    "education": this.education,
                    "university": this.university,
                    "score": this.score,
                    "field_of_study": this.fieldOfStudy,
                }

                if (this.educationalRecords.some(dict => JSON.stringify(dict) === JSON.stringify(newEdRecord))) {
                    this.fieldOfStudyE = true
                    this.fieldOfStudyEM = "این مورد وجود دارد."
                    this.educationE = true
                    this.educationEM = "این مورد وجود دارد."
                    this.universityE = true
                    this.universityEM = "این مورد وجود دارد."
                    this.scoreE = true
                    this.scoreEM = "این مورد وجود دارد."
                } else {
                    this.educationalRecords.push(newEdRecord)
                }
            }
        },

        addWorkExperience() {
            let access = true

            if (this.job === "") {
                this.jobE = true
                this.jobEM = "الزامی می باشد."
                access = false
            } else {
                this.jobE = false
            }

            if (this.company === "") {
                this.companyE = true
                this.companyEM = "الزامی می باشد."
                access = false
            } else {
                this.companyE = false
            }

            if (access) {
                const newWorkExp = { "company": this.company, "job": this.job }

                if (this.workExperiences.some(dict => JSON.stringify(dict) === JSON.stringify(newWorkExp))) {
                    this.companyE = true
                    this.companyEM = "این مورد وجود دارد."
                    this.jobE = true
                    this.jobEM = "این مورد وجود دارد."
                } else {
                    this.workExperiences.push(newWorkExp)
                }
            }
        },

        createProfile() {
            let access = true

            if (this.firstName === "") {
                access = false
                this.firstNameE = true
                this.firstNameEM = "الزامی است"
            } else {
                this.firstNameE = false
            }

            if (this.lastName === "") {
                access = false
                this.lastNameE = true
                this.lastNameEM = "الزامی است"
            } else {
                this.lastNameE = false
            }

            if (this.nationalCode === "") {
                access = false
                this.nationalCodeE = true
                this.nationalCodeEM = "الزامی است"
            } else {
                this.nationalCodeE = false
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

            if (this.gender === "") {
                access = false
                this.genderE = true
                this.genderEM = "الزامی است"
            } else {
                this.genderE = false
            }

            if (this.militaryServiceStatus === "") {
                access = false
                this.militaryServiceStatusE = true
                this.militaryServiceStatusEM = "الزامی است"
            } else {
                this.militaryServiceStatusE = false
            }

            if (this.language === "") {
                access = false
                this.languageE = true
                this.languageEM = "الزامی است"
            } else {
                this.languageE = false
            }

            if (this.dayOfBirth === "") {
                access = false
                this.dayOfBirthE = true
                this.dayOfBirthEM = "الزامی است"
            } else {
                this.dayOfBirthE = false
            }

            if (this.yearOfBirth === "") {
                access = false
                this.yearOfBirthE = true
                this.yearOfBirthEM = "الزامی است"
            } else {
                this.yearOfBirthE = false
            }

            function isValidNationalCode(code) {
                // Check the length of the code
                if (code.length !== 10) {
                    return false;
                }

                // Check for duplicate digits
                if (/(\d)\1{9}/.test(code)) {
                    return false;
                }

                // Calculate the control digit
                var sum = 0;
                for (var i = 0; i < 9; i++) {
                    sum += parseInt(code.charAt(i)) * (10 - i);
                }
                var remainder = sum % 11;
                var controlDigit = (remainder < 2) ? remainder : (11 - remainder);

                // Compare the control digit with the last digit of the code
                if (controlDigit != code.charAt(9)) {
                    return false;
                }

                return true;
            }

            const isNationalCode = isValidNationalCode(this.nationalCode)
            if (!isNationalCode) {
                this.nationalCodeE = true
                this.nationalCodeEM = "کد ملی اشتباه است."
                access = false
            } else {
                this.nationalCodeE = false
                access = true
            }

            let newWorkExpDict = this.workExperiences.filter((item) => {
                if (!item.hasOwnProperty('id')) {
                    return item
                }
            })

            if (access && newWorkExpDict) {
                axios
                    .post('/account/api/profile/work-exp/',
                        newWorkExpDict
                    )
                    .then(response => {
                        //console.log(response.data);
                    })
                    .catch(e => {
                        console.log(e.response);
                    })
            }

            let newEdRecordDict = this.educationalRecords.filter((item) => {
                if (!item.hasOwnProperty('id')) {
                    return item
                }
            })

            if (access && newEdRecordDict) {
                axios
                    .post('/account/api/profile/ed-record/',
                        newEdRecordDict
                    )
                    .then(response => {
                        // console.log(response.data);
                    })
                    .catch(e => {
                        console.log(e.response);
                    })
            }

            if (access && !this.created) {
                axios
                    .post('/account/api/profile/',
                        {
                            "first_name": this.firstName,
                            "last_name": this.lastName,
                            "email": this.email,
                            "national_code": this.nationalCode,
                            "passport_number": "",
                            "country": "string",
                            "province": provinceData.find(province => province.id == this.province).name,
                            "city": cityData.find(city => city.name == this.city).name,
                            "address": this.address,
                            "is_married": this.isMarried,
                            "gender": this.gender,
                            "date_of_birth": `${this.yearOfBirth}-${this.monthOfBirth}-${this.dayOfBirth}`,
                            "military_service_status": this.militaryServiceStatus,
                            "other_exemptions": this.otherExemptions,
                            "about_me": this.aboutMe,
                            "language": []
                            // this.language.map(i => i+1)
                        }
                    )
                    .then(response => {
                    })
                    .catch(error => {
                        console.log(error.response);
                    })
            } else if (access && this.created) {
                const phone = localStorage.getItem("phone");

                axios
                    .put(`/account/api/profile/${phone}/`,
                        {
                            "first_name": this.firstName,
                            "last_name": this.lastName,
                            "email": this.email,
                            "national_code": this.nationalCode,
                            "passport_number": "",
                            "country": "ایران",
                            "province": provinceData.find(province => province.id == this.province).name,
                            "city": cityData.find(city => city.name == this.city).name,
                            "address": this.address,
                            "is_married": this.isMarried,
                            "gender": this.gender,
                            "date_of_birth": `${this.yearOfBirth}-${this.monthOfBirth}-${this.dayOfBirth}`,
                            "military_service_status": this.militaryServiceStatus,
                            "other_exemptions": this.otherExemptions,
                            "about_me": this.aboutMe,
                            "language": []
                            // this.language.map(i => i+1)
                        }
                    )
                    .then(response => {
                    })
                    .catch(error => {
                        console.log(error.response);
                    })
            }
        },
    },
    watch: {
        province() {
            let provinceValue = document.getElementById("province").value
            this.cityList = cityData.filter(item => item.province_id == provinceValue)
        }

    },
    mounted() {
        const phone = localStorage.getItem("phone");

        axios
            .get(`/account/api/profile/${phone}/`)
            .then(response => {
                this.created = true

                const getData = response.data
                const date = getData.date_of_birth.split("-")
                const monthVal = document.getElementById("m" + date[1]).value
                const getProvince = provinceData.find(province => province.name === getData.province);

                this.firstName = getData.first_name
                this.lastName = getData.last_name
                this.email = getData.email
                this.avatar = getData.avatar
                this.nationalCode = getData.national_code
                this.country = getData.country
                this.province = getProvince.id
                this.city = getData.city
                this.address = getData.address
                this.isMarried = getData.is_married
                this.gender = getData.gender
                this.dayOfBirth = date[2]
                this.monthOfBirth = monthVal
                this.yearOfBirth = date[0]
                this.militaryServiceStatus = getData.military_service_status
                this.otherExemptions = getData.other_exemptions
                this.aboutMe = getData.about_me
                // this.cv_file = getData.cv_file
                this.language = getData.language

            })
            .catch(e => {
                console.log(e.response);
            })

        axios
            .get(`/account/api/profile/work-exp/`,
                { params: { search: phone } }
            )
            .then(response => {
                this.workExperiences = response.data
            })
            .catch(e => {
                // console.log(e.response);
            })

        axios
            .get(`/account/api/profile/ed-record/`,
                { params: { search: phone } }
            )
            .then(response => {
                this.educationalRecords = response.data
            })
            .catch(e => {
                // console.log(e.response);
            })
    },
}


</script>


<style scoped>
.work-exp-container>ul {
    justify-content: space-around;
}

.work-exp-container>ul:nth-child(1) {
    padding: 10px 0;
}

.work-exp-list {
    padding: 10px 0;
}

.ed-record-container {
    overflow-x: auto
}

.ed-record-container table {
    width: 100%;
    border-collapse: collapse;
}

.ed-record-container table th,
td {
    text-align: center;
    padding: 8px;
}

.ed-record-container ul li {
    padding: 0 10px;
}

.ed-record-container>ul:nth-child(1) {
    padding: 10px 0;
}

.ed-record-list {
    padding: 10px 0;
}
</style>