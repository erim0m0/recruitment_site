<template>
    <div class="Login">
        <!-- login wrapper start -->
        <div class="login_wrapper jb_cover">
            <div class="container">
                <div class="row">
                    <div class="col-lg-12 col-md-12 col-sm-12">
                        <div class="login_top_box jb_cover">
                            <div class="login_banner_wrapper">
                                <img src="images/logo.png" alt="logo">
                                <div class="header_btn search_btn facebook_wrap jb_cover">

                                    <a href="#">ورود با فیسبوک <i class="fab fa-facebook-f"></i></a>

                                </div>
                                <div class="header_btn search_btn google_wrap jb_cover">

                                    <a href="#">ورود با پینترست <i class="fab fa-pinterest-p"></i></a>

                                </div>
                                <div class="jp_regis_center_tag_wrapper jb_register_red_or">
                                    <h1>یا</h1>
                                </div>
                            </div>
                            
                            <div class="login_form_wrapper">
                                <h2>ثبت نام</h2>
                                <form @submit.prevent="doSignup" class="signin-form">
                                    <div class="form-group icon_form comments_form">
                                        <input v-model="phone" type="text" class="form-control" placeholder="شماره همراه"
                                            :class="{
                                                'is-valid': phoneE === false,
                                                'is-invalid': phoneE === true,
                                            }">
                                            <i class="fas fa-envelope"></i>
                                        <div class="invalid-feedback" v-if="phoneE">
                                            {{ phoneEM }}
                                        </div>
                                    </div>
                                    <div class="form-group icon_form comments_form">
                                        <input v-model="password" type="text" class="form-control" placeholder="رمز عبور"
                                            :class="{
                                                'is-valid': passwordE === false,
                                                'is-invalid': passwordE === true,
                                            }">
                                            <i class="fas fa-lock"></i>
                                        <div class="invalid-feedback" v-if="passwordE">
                                            {{ passwordEM }}
                                        </div>
                                    </div>
                                    <button type="submit" class="btn btn-primary">تایید</button>
                                </form>
                                <div class="login_remember_box">
                                    <label class="control control--checkbox">مرا به خاطر بسپار
                                        <input type="checkbox">
                                        <span class="control__indicator"></span>
                                    </label>
                                    <a href="#" class="forget_password">
                                        فراموشی رمزعبور
                                    </a>
                                </div>
                                <div class="dont_have_account jb_cover">
                                    <p>حساب کاربری ندارید؟ <a href="sign_up.html">ثبت نام</a></p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- login wrapper end -->

        <!-- news app wrapper start-->
        <div class="news_letter_wrapper jb_cover">
            <div class="container">
                <div class="row">
                    <div class="col-lg-12 col-md-12 col-sm-12">
                        <div class="job_newsletter_wrapper jb_cover">
                            <div class="jb_newslwtteter_left">
                                <h2> به دنبال یک شغل</h2>
                                <p>سطح بعدی شما دارایی های شرکت توسعه محصول سطح بعدی شما محصول </p>
                            </div>
                            <div class="jb_newslwtteter_button">
                                <div class="header_btn search_btn news_btn jb_cover">

                                    <a href="#">تایید</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- news app wrapper end-->
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'Signup',
    data() {
        return {
            phone: "",
            phoneE: null,
            phoneEM: null,
            password: "",
            passwordE: null,
            passwordEM: null
        }
    },
    methods: {
        doSignup() {
            let access = true

            // Create a regular expression
            let patternPhone = /^9\d{2}\s*?\d{3}\s*?\d{4}$/;
            let patternPassword = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#!%*?&])[A-Za-z\d@$#!%*?&]{8,}$/;


            // Test the pattern against a string
            let resultPatternPhone = patternPhone.test(this.phone);

            if (this.phone === "") {
                access = false
                this.phoneE = true
                this.phoneEM = 'شماره‌ی همراه را وارد کنید.'
            } else if (!resultPatternPhone) {
                access = false
                this.phoneE = true
                this.phoneEM = 'شماره نامعتبر است.'
            } else {
                this.phoneE = false
                this.phoneEM = ''
            }

            // Test the pattern against a string
            let resultpatternPassword = patternPassword.test(this.password);
            
            if (!resultpatternPassword) {
                access = false
                this.passwordE = true
                this.passwordEM = 'پسورد مورد قبول نیست.'
            } else {
                this.passwordE = false
                this.passwordEM = ''
            }

            if (access) {
                let data = null
                if (this.password) {
                    data = {
                        phone:this.phone,
                        password:this.password
                    }
                } else {
                    data = {
                        phone:this.phone
                    }
                }
                axios
                    .post('/account/api/sign-in/', data)
                    .then(response => {
                        localStorage.setItem("id_code", response.data.id_code)
                        localStorage.setItem("phone", this.phone)
                        if (!this.password) {
                            this.$router.push("/verify")
                        } else {
                            this.$router.push("/")
                        }
                    })
                    .catch(error => {})
            }
        },
    },

}

</script>