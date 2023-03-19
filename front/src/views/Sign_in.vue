<template>
    <div class="Signup">
        <section class="ftco-section">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-md-6 col-lg-4">
                        <div class="login-wrap p-0">
                            <h3 class="mb-4 text-center">لطفا شماره خود را وارد کنید.</h3>
                            <form @submit.prevent="doSendPhone" class="signin-form">
                                <div class="form-group">
                                    <input v-model="phone" dir="ltr" type="text" class="form-control"
                                        placeholder="شماره تماس" :class="{
                                            'is-valid': phoneE === false,
                                            'is-invalid': phoneE === true,
                                        }">
                                    <div class="invalid-feedback" v-if="phoneE">
                                        {{ phoneEM }}
                                    </div>
                                </div>
                                <button type="submit" class="btn btn-primary">ارسال</button>
                            </form>
                            <p class="w-100 text-center">&mdash; Or Sign In With &mdash;</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'Signin',
    data() {
        return {
            phone: "",
            phoneE: null,
            phoneEM: null,
        }
    },
    methods: {
        doSendPhone() {
            let access = true

            // Create a regular expression to match a number with phone's number
            let pattern = /^9\d{2}\s*?\d{3}\s*?\d{4}$/;

            // Test the pattern against a string
            let result = pattern.test(this.phone);

            if (!result) {
                access = false
                this.phoneE = true
                this.phoneEM = 'لطفا شماره‌ی صحیح وارد کنید.'
            } else {
                this.phoneE = false
                this.phoneEM = ''
            }

            if (access) {
                axios
                    .post('/account/api/sign-in/', {
                        phone: this.phone
                    })
                    .then(response => {
                        localStorage.setItem("id_code", response.data.id_code)
                        localStorage.setItem("phone", this.phone)
                        this.$router.push("/verify")
                    })
                    .catch(error => {
                        this.phoneE = true
                        if (error.response.status == 401) {
                            this.phoneEM = "کاربری یافت نشد."
                        }
                    })
            }
        }
    },
}

</script>