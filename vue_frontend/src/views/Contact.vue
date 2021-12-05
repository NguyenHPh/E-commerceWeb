<template>
<div id="get-in-touch">
    <div class="container-base mx-auto my-5 py-3">
        <div class="row">
            <div class="col-10 col-lg-6 general-info px-4 mx-auto">
                <div class="text-center mb-4">
                    <h1 class="d-inline-block mx-auto">drop us a note</h1>
                </div>
                <p>You can use this form to get in touch and we'll aim to get back to you as soon as we can.</p>
                <p class="font-weight-bold note">Please note: We are experiencing very high volumes of queries at the moment, so it may take a little longer than usual to get back to you. Rest assured we'll get back to you as quickly as we can.</p>
                <img src="../assets/image/get-in-touch-dog.png" alt="deliver" class="w-100 img-fluid px-3 mx-auto mt-3">
            </div>
            <div class="col-10 col-lg-6 form-sending px-4 mx-auto">
                <form action="">
                    <div class="my-4">
                        <label>First Name *</label>
                        <input type="text" class="d-block w-100">
                    </div>
                    <div class="mb-4">
                        <label>Last Name *</label>
                        <input type="text" class="d-block w-100">
                    </div>
                    <div class="mb-4">
                        <label>Email Address *</label>
                        <input type="text" class="d-block w-100">
                    </div>
                    <div class="mb-4">
                        <label>Query *</label>
                        <textarea type="text" class="d-block w-100" rows="3"></textarea>
                    </div>
                    <button type="submit">submit</button>
                </form>                        
            </div>
        </div>
    </div>

    <div class="container-fluid more-info">
        <div class="container-base mx-auto py-3">
            <div class="row pt-5">
                <div class="px-3 col-lg-6 mb-3">
                    <div class="item pt-5 pb-3 pl-5 pr-3 mx-auto">
                        <h3>got a question?</h3>
                        <p class="mt-4 description">check out our frequently asked questions for lots of information & advice.</p>
                        <div>
                            <a href="#">to the FAQs</a>
                        </div>
                        <img class="img-fluid w-100" src="../assets/image/contact-more-info-img.png" alt="decorate">
                    </div>
                </div>
                
                <div class="px-3 col-lg-6 mb-3">
                    <div class="item pt-5 pb-3 pl-5 pr-3 mx-auto">
                        <h3>send us an e-mail</h3>
                        <p class="mt-4 description">Click below to send an e-mail and one of our friendly team of Devonian dog lovers will get back to you as soon as possible.</p>
                        <div>
                            <a href="#">Email us</a>
                        </div>
                        <img class="img-fluid w-100" src="../assets/image/contact-more-info-img.png" alt="decorate">
                    </div>
                </div>

                <div class="px-3 col-lg-6 mb-3">
                    <div class="item pt-5 pb-4 pl-5 pr-3 mx-auto">
                        <h3>give us a call</h3>
                        <p class="mt-4 description">our friendly team are on hand to answer your questions between 8am-5pm Mon-Fri - just drop us a line on <b>0808 169 2900</b></p>
                        <img class="img-fluid w-100 pb-2" src="../assets/image/contact-more-info-img.png" alt="decorate">
                    </div>
                </div>

                <div class="px-3 col-lg-6 mb-3">
                    <div class="item pt-5 pb-3 pl-5 pr-3 mx-auto">
                        <h3>trade enquiries</h3>
                        <p class="mt-4 description">if you've got a query for our trade team or would like to have a chat about becoming a stockist please get in touch</p>
                        <div>
                            <a href="#">click here</a>
                        </div>
                        <img class="img-fluid w-100" src="../assets/image/contact-more-info-img.png" alt="decorate">
                    </div>
                </div>

                <div class="px-3 col-lg-6 mb-3">
                    <div class="item pt-5 pb-3 pl-5 pr-3 mx-auto">
                        <h3>press enquiries</h3>
                        <p class="mt-4 description">if you'd like to get in touch with our PR team then please click below and we'll get back to you as soon as we can.</p>
                        <div>
                            <a href="#">click here</a>
                        </div>
                        <img class="img-fluid w-100" src="../assets/image/contact-more-info-img.png" alt="decorate">
                    </div>
                </div>

                <div class="px-3 col-lg-6 mb-3">
                    <div class="item pt-5 pb-3 pl-5 pr-3 mx-auto">
                        <h3>charity enquiries</h3>
                        <p class="mt-4 description">if you'd like to get in touch to request help or support for a charitable cause</p>
                        <div>
                            <a href="#">click here</a>
                        </div>
                        <img class="img-fluid w-100" src="../assets/image/contact-more-info-img.png" alt="decorate">
                    </div>
                </div>                                       
            </div>
        </div>
        <div class="container-fluid contact-learn-more-01 mx-auto my-5 py-5">
            <div class="col-lg-5 py-4 text-center">
                <h2>join the team</h2>
                <h4 class="mt-4 pb-3">check out our latest vacancies</h4>
                <div class="mx-auto py-2 my-3">
                    <a href="#">learn more</a>
                </div>
            </div>
        </div>
    </div> 

    <div class="container-fluid py-5 contact-learn-more">
        <div class="col-lg-6 mx-auto py-4 text-center">
            <h2>looking for a stockist?</h2>
            <h4 class="mt-4 pb-3">find stockists near you</h4>
            <div class="mx-auto py-2 my-3">
                <a href="#">learn more</a>
            </div>
        </div>
    </div>
</div>
</template>


<script>

export default {
    name: 'Contact',
    data() {
        return{

        }
    },
    mounted() {
        document.title = 'Get in touch'
    }
}
</script>

<style scoped src="../assets/styles/bootstrap.min.css">
</style>
<style scoped src="../assets/styles/get-in-touch.css">
</style>