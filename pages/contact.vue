<template>
  <div>
    <!-- Hero Section -->
    <section class="relative h-64 flex items-center justify-center overflow-hidden">
      <div class="absolute inset-0">
        <NuxtImg 
          src="/images/contact-hero.jpg" 
          alt="Contact Go For It Gas"
          class="w-full h-full object-cover"
        />
        <div class="hero-overlay"></div>
      </div>
      <div class="relative z-10 text-center text-white">
        <h1 class="heading-2 mb-4 text-shadow-lg">We'd Love to Hear from You</h1>
        <p class="text-lg text-shadow">Get in touch with questions, feedback, or just to say hello</p>
      </div>
    </section>

    <!-- Contact Form & Info -->
    <section class="py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid lg:grid-cols-2 gap-12">
          <!-- Contact Form -->
          <div class="card">
            <div class="card-body">
              <h2 class="heading-2 mb-6">Send us a Message</h2>
              
              <form @submit.prevent="submitForm" class="space-y-6">
                <div class="grid md:grid-cols-2 gap-4">
                  <div>
                    <label for="firstName" class="block text-sm font-medium text-neutral-700 mb-2">First Name *</label>
                    <input 
                      type="text" 
                      id="firstName" 
                      v-model="form.firstName"
                      required
                      class="w-full px-3 py-2 border border-neutral-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                      placeholder="Your first name"
                    >
                  </div>
                  <div>
                    <label for="lastName" class="block text-sm font-medium text-neutral-700 mb-2">Last Name *</label>
                    <input 
                      type="text" 
                      id="lastName" 
                      v-model="form.lastName"
                      required
                      class="w-full px-3 py-2 border border-neutral-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                      placeholder="Your last name"
                    >
                  </div>
                </div>

                <div>
                  <label for="email" class="block text-sm font-medium text-neutral-700 mb-2">Email *</label>
                  <input 
                    type="email" 
                    id="email" 
                    v-model="form.email"
                    required
                    class="w-full px-3 py-2 border border-neutral-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                    placeholder="your.email@example.com"
                  >
                </div>

                <div>
                  <label for="phone" class="block text-sm font-medium text-neutral-700 mb-2">Phone</label>
                  <input 
                    type="tel" 
                    id="phone" 
                    v-model="form.phone"
                    class="w-full px-3 py-2 border border-neutral-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                    placeholder="(555) 123-4567"
                  >
                </div>

                <div>
                  <label for="subject" class="block text-sm font-medium text-neutral-700 mb-2">Subject *</label>
                  <select 
                    id="subject" 
                    v-model="form.subject"
                    required
                    class="w-full px-3 py-2 border border-neutral-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                  >
                    <option value="">Select a subject</option>
                    <option value="general">General Inquiry</option>
                    <option value="fuel">Fuel Prices</option>
                    <option value="services">Services</option>
                    <option value="promotions">Promotions</option>
                    <option value="feedback">Feedback</option>
                    <option value="complaint">Complaint</option>
                    <option value="other">Other</option>
                  </select>
                </div>

                <div>
                  <label for="message" class="block text-sm font-medium text-neutral-700 mb-2">Message *</label>
                  <textarea 
                    id="message" 
                    v-model="form.message"
                    required
                    rows="5" 
                    class="w-full px-3 py-2 border border-neutral-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                    placeholder="Tell us how we can help you..."
                  ></textarea>
                </div>

                <button 
                  type="submit" 
                  :disabled="isSubmitting"
                  class="btn-primary w-full"
                >
                  <span v-if="isSubmitting" class="loading-dots">
                    <div></div>
                    <div></div>
                    <div></div>
                  </span>
                  <span v-else>Send Message</span>
                </button>
              </form>

              <!-- Success Message -->
              <div v-if="showSuccess" class="mt-6 p-4 bg-green-50 border border-green-200 rounded-lg">
                <div class="flex items-center">
                  <svg class="w-5 h-5 text-green-500 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                  </svg>
                  <span class="text-green-700 font-medium">Thank you! Your message has been sent successfully.</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Contact Information -->
          <div class="space-y-8">
            <!-- Store Info -->
            <div class="card">
              <div class="card-body">
                <h3 class="heading-3 mb-6">Store Information</h3>
                
                <div class="space-y-6">
                  <div class="flex items-start">
                    <div class="w-12 h-12 bg-primary-100 rounded-lg flex items-center justify-center mr-4">
                      <svg class="w-6 h-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
                      </svg>
                    </div>
                    <div>
                      <h4 class="font-semibold text-neutral-900 mb-1">Address</h4>
                      <p class="text-neutral-600 mb-2">3255 Viking Blvd NE<br>East Bethel, MN 55092</p>
                      <a href="https://www.google.com/maps?cid=12853947706317488130" target="_blank" class="text-primary-500 hover:text-primary-600 transition-colors">
                        Get Directions →
                      </a>
                    </div>
                  </div>

                  <div class="flex items-start">
                    <div class="w-12 h-12 bg-primary-100 rounded-lg flex items-center justify-center mr-4">
                      <svg class="w-6 h-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path>
                      </svg>
                    </div>
                    <div>
                      <h4 class="font-semibold text-neutral-900 mb-1">Phone</h4>
                      <p class="text-neutral-600 mb-2">(651) 395-2174</p>
                      <a href="tel:+16513952174" class="text-primary-500 hover:text-primary-600 transition-colors">
                        Call Now →
                      </a>
                    </div>
                  </div>

                  <div class="flex items-start">
                    <div class="w-12 h-12 bg-primary-100 rounded-lg flex items-center justify-center mr-4">
                      <svg class="w-6 h-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                      </svg>
                    </div>
                    <div>
                      <h4 class="font-semibold text-neutral-900 mb-1">Email</h4>
                      <p class="text-neutral-600 mb-2">info@goforitgas.com</p>
                      <a href="mailto:info@goforitgas.com" class="text-primary-500 hover:text-primary-600 transition-colors">
                        Send Email →
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Store Hours -->
            <div class="card">
              <div class="card-body">
                <h3 class="heading-3 mb-6">Store Hours</h3>
                
                <div class="space-y-3">
                  <div class="flex justify-between items-center">
                    <span class="font-medium">Monday</span>
                    <span class="text-neutral-600">6:00 AM - 10:00 PM</span>
                  </div>
                  <div class="flex justify-between items-center">
                    <span class="font-medium">Tuesday</span>
                    <span class="text-neutral-600">6:00 AM - 10:00 PM</span>
                  </div>
                  <div class="flex justify-between items-center">
                    <span class="font-medium">Wednesday</span>
                    <span class="text-neutral-600">6:00 AM - 10:00 PM</span>
                  </div>
                  <div class="flex justify-between items-center">
                    <span class="font-medium">Thursday</span>
                    <span class="text-neutral-600">6:00 AM - 10:00 PM</span>
                  </div>
                  <div class="flex justify-between items-center">
                    <span class="font-medium">Friday</span>
                    <span class="text-neutral-600">6:00 AM - 10:00 PM</span>
                  </div>
                  <div class="flex justify-between items-center">
                    <span class="font-medium">Saturday</span>
                    <span class="text-neutral-600">6:00 AM - 10:00 PM</span>
                  </div>
                  <div class="flex justify-between items-center">
                    <span class="font-medium">Sunday</span>
                    <span class="text-neutral-600">6:00 AM - 10:00 PM</span>
                  </div>
                </div>
                
                <div class="mt-6 p-4 bg-accent-50 border border-accent-200 rounded-lg">
                  <div class="flex items-center">
                    <div class="w-3 h-3 bg-green-500 rounded-full mr-3"></div>
                    <span class="font-semibold text-green-700">Open Now</span>
                  </div>
                  <p class="text-sm text-neutral-600 mt-1">Closes at 10:00 PM today</p>
                </div>
                
                <p class="text-sm text-neutral-500 mt-4">*Gas pumps available 24/7</p>
              </div>
            </div>

            <!-- Quick Actions -->
            <div class="card">
              <div class="card-body">
                <h3 class="heading-3 mb-6">Quick Actions</h3>
                
                <div class="space-y-4">
                  <a href="tel:+16513952174" class="btn-primary w-full text-center block">
                    Call Now
                  </a>
                  <a href="https://www.google.com/maps?cid=12853947706317488130" target="_blank" class="btn-outline w-full text-center block">
                    Get Directions
                  </a>
                  <NuxtLink to="/fuel" class="btn-ghost w-full text-center block">
                    View Fuel Prices
                  </NuxtLink>
                  <NuxtLink to="/promotions" class="btn-ghost w-full text-center block">
                    Current Promotions
                  </NuxtLink>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Map Section -->
    <section class="py-16 bg-neutral-50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="heading-2 mb-4">Find Us</h2>
          <p class="text-xl text-neutral-600">Located conveniently in East Bethel, MN</p>
        </div>
        
        <div class="card">
          <div class="card-body">
            <div class="bg-neutral-200 h-96 rounded-lg flex items-center justify-center">
              <div class="text-center">
                <svg class="w-16 h-16 text-neutral-400 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
                </svg>
                <p class="text-neutral-500 mb-4">Interactive Google Map would be embedded here</p>
                <a href="https://www.google.com/maps?cid=12853947706317488130" target="_blank" class="btn-primary">
                  Open in Google Maps
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
const form = ref({
  firstName: '',
  lastName: '',
  email: '',
  phone: '',
  subject: '',
  message: ''
})

const isSubmitting = ref(false)
const showSuccess = ref(false)

const submitForm = async () => {
  isSubmitting.value = true
  
  try {
    // Simulate form submission
    await new Promise(resolve => setTimeout(resolve, 2000))
    
    // Reset form
    form.value = {
      firstName: '',
      lastName: '',
      email: '',
      phone: '',
      subject: '',
      message: ''
    }
    
    showSuccess.value = true
    
    // Hide success message after 5 seconds
    setTimeout(() => {
      showSuccess.value = false
    }, 5000)
    
  } catch (error) {
    console.error('Form submission error:', error)
  } finally {
    isSubmitting.value = false
  }
}

useHead({
  title: 'Contact Us - Go For It Gas',
  meta: [
    { name: 'description', content: 'Contact Go For It Gas for questions, feedback, or inquiries. Located at 3255 Viking Blvd NE, East Bethel, MN 55092. Call (651) 395-2174 or visit us today.' },
    { name: 'keywords', content: 'contact, phone, address, directions, store hours, feedback, East Bethel' }
  ]
})
</script>
