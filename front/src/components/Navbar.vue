<template>
    <div class="Navbar">
        <!-- cp navi wrapper Start -->
        <nav class="cd-dropdown  d-block d-sm-block d-md-block d-lg-none d-xl-none">
            <h2><router-link to="/"> <span><img src="@/assets/images/logo.png" alt="logo"></span></router-link></h2>
            <a href="#0" class="cd-close">بستن</a>
            <ul class="cd-dropdown-content">
                <li>
                    <form class="cd-search">
                        <input type="search" placeholder="جستجو...">
                    </form>
                </li>
                <li class="has-children">
                    <a href="#">خانه</a>
                    <ul class="cd-secondary-dropdown icon_menu is-hidden">
                        <li class="go-back"><a href="#0">منو</a></li>
                        <li><a href="index.html">خانه 1</a></li>
                        <li><a href="index_II.html">خانه 2</a></li>
                        <li><a href="index_III.html">خانه 3</a></li>
                    </ul>
                </li>
                <li class="has-children">
                    <a href="#">مشاغل</a>
                    <ul class="cd-secondary-dropdown icon_menu is-hidden">
                        <li class="go-back"><a href="#0">منو</a></li>
                        <li><a href="job_listing_grid_left_filter.html">آگهی شغلی گرید </a></li>
                        <li><a href="job_listing_list_left_filter.html">آگهی شغلی لیست</a></li>
                        <li><a href="job_single.html">شغل تنها</a></li>
                    </ul>
                </li>
                <!-- .has-children -->
                <li class="has-children">
                    <a href="#">صفحات</a>
                    <ul class="cd-secondary-dropdown icon_menu is-hidden">
                        <li class="go-back"><a href="#0">منو</a></li>
                        <li><a href="about_us.html">درباره ما</a></li>
                        <li><a href="companies.html">شرکت ها</a></li>
                        <li><a href="company_single.html">شرکت تنها</a></li>
                        <li><a href="error_page.html">صفحه ارور</a></li>
                        <li><a href="login.html">ورود</a></li>
                        <li><a href="pricing_table.html">جدول قیمت گذاری</a></li>
                        <li><a href="sign_up.html">ثبت نام</a></li>

                    </ul>
                </li>
                <li class="has-children">
                    <a href="#">داشبورد</a>
                    <ul class="cd-secondary-dropdown is-hidden">
                        <li class="go-back"><a href="#0">منو</a>
                        </li>
                        <li class="has-children"> <a href="#">داوطلب</a>
                            <ul class="cd-secondary-dropdown is-hidden">
                                <li class="go-back"><a href="#0">منو</a>
                                </li>
                                <li>
                                    <a href="../dashboard/candidate_applied_job.html">شغل تاییده شده </a>
                                </li>
                                <li>
                                    <a href="../dashboard/candidate_dashboard.html">داشبورد</a>
                                </li>
                                <li>
                                    <a href="../dashboard/candidate_edit_profile.html"> ویرایش پروفایل</a>
                                </li>
                                <li>
                                    <a href="../dashboard/candidate_favourite_job.html">شغل موردعلاقه</a>
                                </li>
                                <li>
                                    <a href="../dashboard/candidate_resume.html"> رزومه</a>
                                </li>
                                <li>
                                    <a href="../dashboard/message.html"> پیام</a>
                                </li>
                                <li>
                                    <a href="../dashboard/pricing_plans.html">برنامه های قیمت گذاری</a>
                                </li>
                            </ul>
                            <!-- .cd-secondary-dropdown -->
                        </li>
                        <!-- .has-children -->
                        <li class="has-children"> <a href="#">شرکت</a>
                            <ul class="cd-secondary-dropdown is-hidden">
                                <li class="go-back"><a href="#0">منو</a>
                                </li>
                                <li>
                                    <a href="../dashboard/comp_applications.html"> برنامه ها </a>
                                </li>
                                <li>
                                    <a href="../dashboard/comp_company_page.html">صفحه شرکت</a>
                                </li>
                                <li>
                                    <a href="../dashboard/comp_employer_dashboard.html"> داشبورد</a>
                                </li>
                                <li>
                                    <a href="../dashboard/comp_employer_edit_profile.html">ویرایش پروفایل</a>
                                </li>
                                <li>
                                    <a href="../dashboard/comp_employer_manage_jobs.html"> مدیریت مشاغل</a>
                                </li>
                                <li>
                                    <a href="../dashboard/comp_post_new_job.html"> ارسال شغل جدید</a>
                                </li>
                                <li>
                                    <a href="../dashboard/message.html">پیام</a>
                                </li>
                                <li>
                                    <a href="../dashboard/pricing_plans.html">برنامه های قیمت گذاری</a>
                                </li>
                            </ul>
                            <!-- .cd-secondary-dropdown -->
                        </li>
                    </ul>
                    <!-- .cd-secondary-dropdown -->
                </li>
                <li class="has-children">
                    <a href="#">وبلاگ</a>
                    <ul class="cd-secondary-dropdown icon_menu is-hidden">
                        <li class="go-back"><a href="#0">منو</a></li>
                        <li><a href="blog_single.html">وبلاگ تنها</a></li>
                        <li><a href="blog_category_right_sidebar.html">دسته بندی وبلاگ</a></li>
                    </ul>
                </li>
                <li><a href="contact_us.html">تماس با ما </a></li>
                <li><a href="login.html">ورود</a></li>
            </ul>
            <!-- .cd-dropdown-content -->
        </nav>
        <div class="cp_navi_main_wrapper jb_cover">
            <div class="container-fluid">
                <div class="cp_logo_wrapper">
                    <router-link to="/">
                        <img src="@/assets/images/logo.png" alt="logo">
                    </router-link>
                </div>
                <!-- mobile menu area start -->
                <header class="mobail_menu d-block d-sm-block d-md-block d-lg-none d-xl-none">
                    <div class="container-fluid">
                        <div class="row">
                            <div class="col-lg-12">
                                <div class="cd-dropdown-wrapper">
                                    <a class="house_toggle" href="#0">
                                        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
                                            version="1.1" id="Capa_1" x="0px" y="0px" viewBox="0 0 31.177 31.177"
                                            style="enable-background:new 0 0 31.177 31.177;" xml:space="preserve"
                                            width="25px" height="25px">
                                            <g>
                                                <g>
                                                    <path class="menubar"
                                                        d="M30.23,1.775H0.946c-0.489,0-0.887-0.398-0.887-0.888S0.457,0,0.946,0H30.23    c0.49,0,0.888,0.398,0.888,0.888S30.72,1.775,30.23,1.775z"
                                                        fill="#004165" />
                                                </g>
                                                <g>
                                                    <path class="menubar"
                                                        d="M30.23,9.126H12.069c-0.49,0-0.888-0.398-0.888-0.888c0-0.49,0.398-0.888,0.888-0.888H30.23    c0.49,0,0.888,0.397,0.888,0.888C31.118,8.729,30.72,9.126,30.23,9.126z"
                                                        fill="#004165" />
                                                </g>
                                                <g>
                                                    <path class="menubar"
                                                        d="M30.23,16.477H0.946c-0.489,0-0.887-0.398-0.887-0.888c0-0.49,0.398-0.888,0.887-0.888H30.23    c0.49,0,0.888,0.397,0.888,0.888C31.118,16.079,30.72,16.477,30.23,16.477z"
                                                        fill="#004165" />
                                                </g>
                                                <g>
                                                    <path class="menubar"
                                                        d="M30.23,23.826H12.069c-0.49,0-0.888-0.396-0.888-0.887c0-0.49,0.398-0.888,0.888-0.888H30.23    c0.49,0,0.888,0.397,0.888,0.888C31.118,23.43,30.72,23.826,30.23,23.826z"
                                                        fill="#004165" />
                                                </g>
                                                <g>
                                                    <path class="menubar"
                                                        d="M30.23,31.177H0.946c-0.489,0-0.887-0.396-0.887-0.887c0-0.49,0.398-0.888,0.887-0.888H30.23    c0.49,0,0.888,0.398,0.888,0.888C31.118,30.78,30.72,31.177,30.23,31.177z"
                                                        fill="#004165" />
                                                </g>
                                            </g>
                                        </svg>
                                    </a>
                                    <!-- .cd-dropdown -->

                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- .cd-dropdown-wrapper -->
                </header>
                <div v-if="!$store.state.isAuthenticated" class="menu_btn_box header_btn jb_cover">
                    <ul>
                        <li>
                            <!-- <a href="sign_up.html"><i class="flaticon-man-user"></i> ثبت نام</a> -->
                            <router-link to="/sign-up">ثبت نام</router-link>
                        </li>
                        <li>
                            <!-- <a href="login.html"> <i class="flaticon-login"></i> ورود</a> -->
                            <router-link to="/sign-in">ورود</router-link>
                        </li>
                    </ul>
                </div>

                <div class="jb_navigation_wrapper">
                    <div class="mainmenu d-xl-block d-lg-block d-md-none d-sm-none d-none">
                        <ul class="main_nav_ul">
                            <li class="has-mega gc_main_navigation"><a href="#"
                                    class="gc_main_navigation active_class">خانه</a>
                                <ul class="navi_2_dropdown">
                                    <li class="parent">
                                        <a href="index.html"><i class="fas fa-square"></i>خانه 1 </a>
                                    </li>
                                    <li class="parent">
                                        <a href="index_II.html"><i class="fas fa-square"></i>خانه 2</a>
                                    </li>
                                    <li class="parent">
                                        <a href="index_III.html"><i class="fas fa-square"></i> خانه 3</a>
                                    </li>

                                </ul>
                            </li>
                            <li class="has-mega gc_main_navigation"><a href="#" class="gc_main_navigation">مشاغل</a>
                                <ul class="navi_2_dropdown">
                                    <li class="parent">
                                        <a href="job_listing_grid_left_filter.html"> <i class="fas fa-square"></i>آگهی شغلی
                                            گرید </a>
                                    </li>
                                    <li class="parent">
                                        <a href="job_listing_list_left_filter.html"> <i class="fas fa-square"></i>آگهی شغلی
                                            لیست </a>
                                    </li>
                                    <li class="parent">
                                        <a href="job_single.html"> <i class="fas fa-square"></i>شغل تنها</a>
                                    </li>

                                    <li class="parent">
                                        <a href="#"><i class="fas fa-square"></i>مشاغل<span><i
                                                    class="fas fa-chevron-right"></i>
                                            </span></a>
                                        <ul class="dropdown-menu-right">
                                            <li>
                                                <a href="job_listing_grid_left_filter.html"> <i
                                                        class="fas fa-square"></i>آگهی شغلی گرید </a>
                                            </li>
                                            <li>
                                                <a href="job_listing_list_left_filter.html"> <i
                                                        class="fas fa-square"></i>آگهی شغلی لیست </a>
                                            </li>
                                            <li>
                                                <a href="job_single.html"> <i class="fas fa-square"></i>شغل تنها</a>
                                            </li>
                                        </ul>
                                    </li>

                                </ul>
                            </li>
                            <li class="has-mega gc_main_navigation kv_sub_menu">
                                <a href="#" class="gc_main_navigation"> داوطلبین</a>
                                <!-- mega menu start -->
                                <ul class="kv_mega_menu">

                                    <li class="kv_mega_menu_width">
                                        <div class="container">

                                            <div class="jn_menu_partion_div">

                                                <div class="candidate_width">
                                                    <div class="jen_tabs_conent_list jb_cover">
                                                        <h1>مهارت های شغلی</h1>
                                                        <ul>
                                                            <li>
                                                                <a href="#"><i class="fas fa-square"></i>HTML5 & CSS3</a>
                                                            </li>
                                                            <li>
                                                                <a href="#"><i class="fas fa-square"></i>وردپرس</a>
                                                            </li>
                                                            <li>
                                                                <a href="#"><i class="fas fa-square"></i>جاوااسکریپت</a>
                                                            </li>
                                                            <li>
                                                                <a href="#"><i class="fas fa-square"></i>فتوشاپ</a>
                                                            </li>
                                                            <li>
                                                                <a href="#"><i class="fas fa-square"></i>طراح</a>
                                                            </li>
                                                            <li>
                                                                <a href="#"><i class="fas fa-square"></i>ساخت و ساز</a>
                                                            </li>
                                                        </ul>
                                                    </div>
                                                </div>
                                                <div class="candidate_width">
                                                    <div class="jen_tabs_conent_list jb_cover">
                                                        <h1>دسته بندی ها</h1>
                                                        <ul>
                                                            <li>
                                                                <a href="#"><i class="fas fa-square"></i>طراحی گرافیک</a>
                                                            </li>
                                                            <li>
                                                                <a href="#"><i class="fas fa-square"></i>مشاغل مهندسی</a>
                                                            </li>
                                                            <li>
                                                                <a href="#"><i class="fas fa-square"></i>مشاغل اصلی</a>
                                                            </li>
                                                            <li>
                                                                <a href="#"><i class="fas fa-square"></i>مشاغل پر کاربرد</a>
                                                            </li>
                                                            <li>
                                                                <a href="#"><i class="fas fa-square"></i>مشاغل دولتی</a>
                                                            </li>
                                                            <li>
                                                                <a href="#"><i class="fas fa-square"></i>شرکت فناوری
                                                                    اطلاعات</a>
                                                            </li>
                                                        </ul>
                                                    </div>
                                                </div>
                                                <div class="candidate_width">
                                                    <div class="jen_tabs_conent_list   jb_cover">
                                                        <h1>موقعیت شغل</h1>
                                                        <ul>
                                                            <li>
                                                                <a href="#"><i class="fas fa-square"></i>هند</a>
                                                            </li>
                                                            <li>
                                                                <a href="#"><i class="fas fa-square"></i>امریکا</a>
                                                            </li>
                                                            <li>
                                                                <a href="#"><i class="fas fa-square"></i>ژاپن</a>
                                                            </li>
                                                            <li>
                                                                <a href="#"><i class="fas fa-square"></i>دبی</a>
                                                            </li>
                                                            <li>
                                                                <a href="#"><i class="fas fa-square"></i>افریقای جنوبی</a>
                                                            </li>
                                                            <li>
                                                                <a href="#"><i class="fas fa-square"></i>چین</a>
                                                            </li>
                                                        </ul>
                                                    </div>
                                                </div>
                                                <div class="candidate_width">
                                                    <div class="jen_tabs_conent_list   jb_cover">
                                                        <h1>مشاغل باز</h1>
                                                        <div class="open_jobs_wrapper">
                                                            <div class="open_jobs_wrapper_1 jb_cover">
                                                                <img src="@/assets/images/job1.jpg" alt="img">
                                                                <div class="open_job_text">
                                                                    <h3><a href="#">برخی از طراحان آن را تحمل کردند</a></h3>
                                                                    <p>5 ساعت پیش</p>

                                                                </div>
                                                            </div>
                                                            <div class="open_jobs_wrapper_1 jb_cover">
                                                                <img src="@/assets/images/job1.jpg" alt="img">
                                                                <div class="open_job_text">
                                                                    <h3><a href="#">برخی از طراحان آن را تحمل کردند</a></h3>
                                                                    <p>12 ساعت پیش</p>

                                                                </div>
                                                            </div>
                                                            <div class="view_all_job jb_cover"><a href="#">مشاهده همه
                                                                    مشاغل</a></div>
                                                        </div>
                                                    </div>

                                                </div>
                                            </div>

                                        </div>
                                    </li>

                                </ul>
                            </li>
                            <li class="has-mega gc_main_navigation"><a href="#" class="gc_main_navigation">صفحات</a>
                                <ul class="navi_2_dropdown">
                                    <li class="parent">
                                        <a href="about_us.html"> <i class="fas fa-square"></i>درباره ما</a>
                                    </li>
                                    <li class="parent">
                                        <a href="companies.html"> <i class="fas fa-square"></i>شرکت ها</a>
                                    </li>
                                    <li class="parent">
                                        <a href="company_single.html"> <i class="fas fa-square"></i>شرکت تنها</a>
                                    </li>
                                    <li class="parent">
                                        <a href="error_page.html"><i class="fas fa-square"></i>صفحه ارور</a>
                                    </li>
                                    <li class="parent">
                                        <a href="login.html"><i class="fas fa-square"></i>ورود</a>
                                    </li>
                                    <li class="parent">
                                        <a href="pricing_table.html"><i class="fas fa-square"></i>جدول قیمت گذاری</a>
                                    </li>
                                    <li class="parent">
                                        <a href="sign_up.html"><i class="fas fa-square"></i>ثبت نام</a>
                                    </li>

                                </ul>
                            </li>
                            <li class="has-mega gc_main_navigation"><a href="#" class="gc_main_navigation">داشبورد</a>
                                <ul class="navi_2_dropdown">
                                    <li class="parent">
                                        <a href="#"><i class="fas fa-square"></i>داوطلب<span><i
                                                    class="fas fa-chevron-right"></i>
                                            </span></a>
                                        <ul class="dropdown-menu-right">
                                            <li>
                                                <a href="../dashboard/candidate_applied_job.html"> <i
                                                        class="fas fa-square"></i>شغل تاییده شده </a>
                                            </li>
                                            <li>
                                                <a href="../dashboard/candidate_dashboard.html"> <i
                                                        class="fas fa-square"></i> داشبورد</a>
                                            </li>
                                            <li>
                                                <a href="../dashboard/candidate_edit_profile.html"> <i
                                                        class="fas fa-square"></i>ویرایش پروفایل</a>
                                            </li>
                                            <li>
                                                <a href="../dashboard/candidate_favourite_job.html"> <i
                                                        class="fas fa-square"></i>شغل موردعلاقه</a>
                                            </li>
                                            <li>
                                                <a href="../dashboard/candidate_resume.html"> <i
                                                        class="fas fa-square"></i>رزومه</a>
                                            </li>
                                            <li>
                                                <a href="../dashboard/message.html"> <i class="fas fa-square"></i>پیام</a>
                                            </li>
                                            <li>
                                                <a href="../dashboard/pricing_plans.html"> <i
                                                        class="fas fa-square"></i>برنامه های قیمت گذاری</a>
                                            </li>
                                        </ul>
                                    </li>
                                    <li class="parent">
                                        <a href="#"><i class="fas fa-square"></i>شرکت<span><i
                                                    class="fas fa-chevron-right"></i>
                                            </span></a>
                                        <ul class="dropdown-menu-right">
                                            <li>
                                                <a href="../dashboard/comp_applications.html"> <i
                                                        class="fas fa-square"></i>برنامه ها </a>
                                            </li>
                                            <li>
                                                <a href="../dashboard/comp_company_page.html"> <i class="fas fa-square"></i>
                                                    صفحه شرکت</a>
                                            </li>
                                            <li>
                                                <a href="../dashboard/comp_employer_dashboard.html"> <i
                                                        class="fas fa-square"></i>داشبورد</a>
                                            </li>
                                            <li>
                                                <a href="../dashboard/comp_employer_edit_profile.html"> <i
                                                        class="fas fa-square"></i>ویرایش پروفایل</a>
                                            </li>
                                            <li>
                                                <a href="../dashboard/comp_employer_manage_jobs.html"> <i
                                                        class="fas fa-square"></i>مدیریت مشاغل</a>
                                            </li>
                                            <li>
                                                <a href="../dashboard/comp_post_new_job.html"> <i
                                                        class="fas fa-square"></i>ارسال شغل جدید</a>
                                            </li>
                                            <li>
                                                <a href="../dashboard/message.html"> <i class="fas fa-square"></i>پیام</a>
                                            </li>
                                            <li>
                                                <a href="../dashboard/pricing_plans.html"> <i
                                                        class="fas fa-square"></i>برنامه های قیمت گذاری</a>
                                            </li>
                                        </ul>
                                    </li>

                                </ul>
                            </li>
                            <li class="has-mega gc_main_navigation"><a href="#" class="gc_main_navigation">وبلاگ</a>
                                <ul class="navi_2_dropdown">
                                    <li class="parent">
                                        <a href="blog_single.html"> <i class="fas fa-square"></i>وبلاگ تنها</a>
                                    </li>
                                    <li class="parent">
                                        <a href="blog_category_right_sidebar.html"> <i class="fas fa-square"></i>دسته بندی
                                            وبلاگ</a>
                                    </li>
                                </ul>
                            </li>
                            <li><a href="contact_us.html" class="gc_main_navigation">تماس</a></li>
                            <li>
                                <router-link to="/sign-in" class="gc_main_navigation" v-if="$store.state.isAuthenticated"
                                    @click="doLogout">خروج</router-link>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        <!-- navi wrapper End -->
    </div>
</template>

<script>

export default {
    name: 'Navbar',
    methods: {
        doLogout() {
            this.$store.commit("logout")
            this.$router.push("/sign-in")
        },
    }
}

</script>