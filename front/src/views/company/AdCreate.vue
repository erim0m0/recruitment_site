<template>
    <div class="AdCreate">
        <!-- top header wrapper start -->
        <div class="page_title_section">
            <div class="page_header">
                <div class="container">
                    <div class="row">
                        <!-- section_heading start -->
                        <div class="col-xl-9 col-lg-7 col-md-7 col-12 col-sm-12">
                            <h1>ارسال شغل جدید</h1>
                        </div>
                        <div class="col-xl-3 col-lg-5 col-md-5 col-12 col-sm-12">
                            <div class="sub_title_section">
                                <ul class="sub_title">
                                    <li> <a href="#"> خانه </a>&nbsp; / &nbsp; </li>
                                    <li>ارسال شغل جدید</li>
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
                                <img src="images/web.png" alt="post_img" />
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
                                        <a href="comp_employer_edit_profile.html"> <i class="fas fa-edit"></i>ویرایش پروفایل
                                        </a>
                                    </li>
                                    <li><a href="comp_company_page.html"><i class="fas fa-file"></i>صفحه شرکت </a></li>
                                    <li><a href="comp_employer_manage_jobs.html"><i class="fas fa-suitcase"></i>مدیریت
                                            مشاغل</a></li>
                                    <li><a href="comp_applications.html"><i class="fas fa-mobile"></i>برنامه ها</a></li>
                                    <li><a href="comp_post_new_job.html" class="link_active"><i
                                                class="fas fa-user-plus"></i>ارسال شغل جدید</a></li>
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

                                                    <input type="password" name="password"
                                                        placeholder="رمز عبور را وارد کنید">
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
                            <div class="col-lg-12 col-md-12 col-sm-12 col-12">
                                <div class="job_filter_category_sidebar pd0 jb_cover">
                                    <div class="job_filter_sidebar_heading jb_cover">
                                        <h1> ارسال شغل جدید</h1>
                                    </div>
                                    <div class="job_overview_header jb_cover">
                                        <div class="row">
                                            <div class="col-lg-12 col-md-12 col-sm-12 col-12">
                                                <div class="contect_form3">
                                                    <label>عنوان*</label>
                                                    <input v-model="title" type="text">
                                                    <div class="invalid-feedback" :class="{
                                                        'd-block': titleE === true
                                                    }" v-if="titleE">
                                                        {{ titleEM }}
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="col-lg-12 col-md-12 col-sm-12 col-12">
                                                <div class="contect_form3">
                                                    <label>رده سازمانی*</label>
                                                    <select v-model="organizationalCategory">
                                                        <option value="کارگر">کارگر</option>
                                                        <option value="کارمند">کارمند</option>
                                                        <option value="کارشناس">کارشناس</option>
                                                        <option value="کارشناس ارشد">کارشناس ارشد</option>
                                                        <option value="معاونت">معاونت</option>
                                                        <option value="مدیر">مدیر</option>
                                                        <option value="مدیر ارشد">مدیر ارشد</option>
                                                    </select>
                                                    <div class="invalid-feedback" :class="{
                                                        'd-block': organizationalCategoryE === true
                                                    }" v-if="organizationalCategoryE">
                                                        {{ organizationalCategoryEM }}
                                                    </div>
                                                </div>
                                                <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                                    <div class="contect_form3">
                                                        <label>نوع همکاری*</label>
                                                        <select v-model="typeOfCooperation">
                                                            <option value="پاره وقت">پاره وقت</option>
                                                            <option value="تمام وقت">تمام وقت</option>
                                                            <option value="دورکاری">دورکاری</option>
                                                        </select>
                                                        <div class="invalid-feedback" :class="{
                                                            'd-block': typeOfCooperationE === true
                                                        }" v-if="typeOfCooperationE">
                                                            {{ typeOfCooperationEM }}
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                                    <div class="contect_form3">
                                                        <label>ساعات کاری</label>
                                                        <input type="text" name="name" placeholder="40/س در هفته">
                                                    </div>
                                                </div>
                                                <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                                    <div class="select_box">
                                                        <label>حقوق</label>
                                                        <select>
                                                            <option>12هزار - 15هزار تومان</option>
                                                            <option>12هزار - 20هزار تومان</option>
                                                            <option> 12هزار - 35هزار تومان</option>
                                                            <option>12هزار - 45هزار تومان</option>
                                                        </select>
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
                                                    <div class="select_box">
                                                        <label>آیا شرکت محل سکونت دارد؟</label>
                                                        <input v-model="isCompanyHaveLivingPlace" type="checkbox">
                                                    </div>
                                                </div>
                                                <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                                    <div class="select_box">
                                                        <label>حداقل سن</label>
                                                        <select v-model="minimumAge" :value="minimumAge">
                                                            <option v-for="i in 33" :value="i + 17">{{ i + 17 }}</option>
                                                        </select>
                                                    </div>
                                                </div>
                                                <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                                    <div class="select_box">
                                                        <label>حداکثر سن</label>
                                                        <select v-model="maximumAge" :value="maximumAge">
                                                            <option v-for="i in 33" :value="i + 17">{{ i + 17 }}</option>
                                                        </select>
                                                    </div>
                                                </div>
                                                <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                                    <div class="select_box">
                                                        <label>جنسیت</label>
                                                        <select v-model="gender" :value="gender">
                                                            <option value="male">مرد</option>
                                                            <option value="female">زن</option>
                                                            <option value="preferably_male">ترجیحا مرد</option>
                                                            <option value="preferably_female">ترجیحا زن</option>
                                                        </select>
                                                    </div>
                                                </div>
                                                <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                                    <div class="select_box">
                                                        <label>وضعیت خدمت سربازی</label>
                                                        <select v-model="militaryServiceStatus"
                                                            :value="militaryServiceStatus">
                                                            <option value="دارای کارت پایان خدمت">دارای کارت پایان خدمت
                                                            </option>
                                                            <option value="در حال خدمت">در حال خدمت</option>
                                                            <option value="معافیت پزشکی">معافیت پزشکی</option>
                                                            <option value="سایر معافیت ها( معافیت غیر پزشکی )">سایر معافیت
                                                                ها( معافیت غیر پزشکی )</option>
                                                            <option value="اهمیتی ندارد">اهمیتی ندارد</option>
                                                        </select>
                                                    </div>
                                                </div>
                                                <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                                    <div class="select_box">
                                                        <label>سابقه کاری*</label>
                                                        <input v-model="workExperience" type="number">
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-lg-12 col-md-12 col-sm-12 col-12">
                                        <div class="job_filter_category_sidebar jb_cover">
                                            <div class="job_filter_sidebar_heading jb_cover">
                                                <h1>زبان مورد نیاز </h1>
                                            </div>
                                            <div class="job_overview_header jb_cover">
                                                <div class="row">
                                                    <ul id="languages" v-for="lng in languages">
                                                        <li v-if="lng == 1">انگلیسی</li>
                                                        <li v-if="lng == 2">فرانسوی</li>
                                                        <li v-if="lng == 3">آلمانی</li>
                                                    </ul>
                                                    <div class="select_box">
                                                        <select v-model="language">
                                                            <option value=1>انگلیسی</option>
                                                            <option value=2>فرانسوی</option>
                                                            <option value=3>آلمانی</option>
                                                        </select>
                                                        <div class="invalid-feedback" :class="{
                                                            'd-block': languageE === true
                                                        }" v-if="languageE">
                                                            {{ languageEM }}
                                                        </div>
                                                    </div>
                                                    <button type="button" v-on:click="addLanguage">افزودن</button>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                <div class="col-lg-12 col-md-12 col-sm-12 col-12">
                                    <div class="job_filter_category_sidebar jb_cover">
                                        <div class="job_filter_sidebar_heading jb_cover">
                                            <h1>کلمات کلیدی تکراری</h1>
                                        </div>
                                        <div class="job_overview_header jb_cover">
                                            <div class="contect_form3">

                                                <input type="text" name="name" placeholder="کلمات کلیدی را تایپ کنید">
                                            </div>
                                            <div class="jb_btm_keyword jb_cover">
                                                <ul>
                                                    <li><i class="flaticon-tag"></i> کلمات کلیدی مورد علاقه :</li>
                                                    <li><a href="#">طراح رابط کاربری،</a></li>
                                                    <li><a href="#">توسعه دهنده،</a></li>
                                                    <li><a href="#">ارشد</a></li>
                                                    <li><a href="#">شرکت آی تی،</a></li>
                                                    <li><a href="#">طراحی،</a></li>
                                                    <li><a href="#">مرکز تماس</a></li>
                                                </ul>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-lg-12 col-md-12 col-sm-12 col-12">
                                    <div class="job_filter_category_sidebar jb_cover">
                                        <div class="job_filter_sidebar_heading jb_cover">
                                            <h1>آدرس / محل </h1>
                                        </div>
                                        <div class="job_overview_header jb_cover">
                                            <div class="row">
                                                <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                                    <div class="select_box">
                                                        <label>کشور</label>
                                                        <select>
                                                            <option>امریکا</option>
                                                            <option>فرانسه</option>
                                                            <option>انگلیس</option>
                                                            <option>آلمان</option>

                                                        </select>
                                                    </div>
                                                </div>
                                                <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                                                    <div class="select_box">
                                                        <label>شهر</label>
                                                        <select>
                                                            <option>نیویورک</option>
                                                            <option>کالفرنیا</option>
                                                            <option> لس آنجلس</option>

                                                        </select>
                                                    </div>
                                                </div>
                                                <div class="col-lg-12 col-md-12 col-sm-12 col-12">
                                                    <div class="contect_form3">
                                                        <label>آدرس کامل</label>
                                                        <input type="text" name="name" placeholder="تهران ایران">
                                                    </div>
                                                </div>

                                                <div class="col-lg-4 col-md-6 col-sm-12 col-12">
                                                    <div class="contect_form3">
                                                        <label>عرض جغرافیایی</label>
                                                        <input type="text" name="name" placeholder="41.4073509">
                                                    </div>
                                                </div>
                                                <div class="col-lg-4 col-md-6 col-sm-12 col-12">
                                                    <div class="contect_form3">
                                                        <label>طول جغرافیایی</label>
                                                        <input type="text" name="name" placeholder="50.4073509">
                                                    </div>
                                                </div>
                                                <div class="col-lg-4 col-md-6 col-sm-12 col-12">
                                                    <div class="contect_form3">
                                                        <label>زوم</label>
                                                        <input type="text" name="name" placeholder="20">
                                                    </div>
                                                </div>
                                                <div class="col-lg-12 col-md-12 col-sm-12 col-12">
                                                    <div class="map_wrapper jb_cover">
                                                        <div id='map'>
                                                        </div>
                                                    </div>
                                                </div>

                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!--employee dashboard wrapper end-->
        </div>
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
            title: "",
            titleE: false,
            titleEM: "",
            organizationalCategory: "",
            organizationalCategoryE: false,
            organizationalCategoryEM: "",
            typeOfCooperation: "",
            typeOfCooperationE: false,
            typeOfCooperationEM: "",
            workTime: "",
            workTimeE: false,
            workTimeEM: "",
            country: "",
            countryE: false,
            countryEM: "",
            province: "",
            provinceE: false,
            provinceEM: "",
            city: "",
            cityE: false,
            cityEM: "",
            isCompanyHaveLivingPlace: "",
            minimumAge: "",
            minimumAgeE: false,
            minimumAgeEM: "",
            maximumAge: "",
            maximumAgeE: false,
            maximumAgeEM: "",
            gender: "",
            genderE: false,
            genderEM: "",
            militaryServiceStatus: "",
            militaryServiceStatusE: false,
            militaryServiceStatusEM: "",
            workExperience: "",
            workExperienceE: false,
            workExperienceEM: "",
            language: "",
            languageE: false,
            languageEM: "",
            languageLevel: "",
            languageLevelE: false,
            languageLevelEM: "",
            benefits: "",
            benefitsE: false,
            benefitsEM: "",
            salary: "",
            salaryE: false,
            salaryEM: "",
            jobDescription: "",
            jobDescriptionE: false,
            jobDescriptionEM: "",
        }
    }
}

</script>