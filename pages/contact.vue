<template>
  <div>
    <!-- Hero Section -->
    <section class="relative min-h-screen flex items-center justify-center overflow-hidden" style="background: linear-gradient(135deg, #0A0A0A 0%, #1A1A1A 50%, #0F0F0F 100%);">
      <div class="absolute inset-0">
        <NuxtImg 
          src="/test_image.jpg" 
          alt="Contact Go For It Liquor - Premium Spirits & Services"
          class="w-full h-full object-cover opacity-20"
          loading="eager"
          preload
        />
        <div class="absolute inset-0" style="background: linear-gradient(135deg, rgba(10, 10, 10, 0.95) 0%, rgba(26, 26, 26, 0.85) 50%, rgba(15, 15, 15, 0.95) 100%);"></div>
      </div>
      
      <div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <div class="mb-8">
          <div class="w-24 h-1 mx-auto mb-6" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
        </div>
        <h1 class="text-6xl md:text-8xl font-bold mb-8 leading-tight" style="color: #F5F5F5; font-family: 'Playfair Display', serif; letter-spacing: -0.02em;">
          We'd Love to<br><span style="color: #D4AF37;">Hear from You</span>
        </h1>
        <div class="w-32 h-1 mx-auto mb-8" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
        <p class="text-xl md:text-2xl mb-12 max-w-3xl mx-auto leading-relaxed" style="color: #E5E5E5; font-family: 'Inter', sans-serif; font-weight: 300;">
          Get in touch with questions, feedback, or just to say hello.<br>
          <span style="color: #D4AF37;">Expert guidance • Premium service • Always here to help</span>
        </p>
        <div class="flex flex-col sm:flex-row gap-6 justify-center">
          <a href="tel:+16513952174" class="group px-10 py-4 text-lg font-semibold rounded-lg transition-all duration-500 border-2" style="border-color: #D4AF37; color: #D4AF37; background: transparent; font-family: 'Inter', sans-serif;" onmouseover="this.style.backgroundColor='#D4AF37'; this.style.color='#0A0A0A'; this.style.boxShadow='0 0 30px rgba(212, 175, 55, 0.4)';" onmouseout="this.style.backgroundColor='transparent'; this.style.color='#D4AF37'; this.style.boxShadow='none';">
            <span class="flex items-center justify-center">
              <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path>
              </svg>
              Call Now
            </span>
          </a>
          <a href="https://maps.app.goo.gl/H1gsh7KUfgrg6ek49" target="_blank" class="group px-10 py-4 text-lg font-semibold rounded-lg transition-all duration-500 border-2" style="border-color: #D4AF37; color: #D4AF37; background: transparent; font-family: 'Inter', sans-serif;" onmouseover="this.style.backgroundColor='#D4AF37'; this.style.color='#0A0A0A'; this.style.boxShadow='0 0 30px rgba(212, 175, 55, 0.4)';" onmouseout="this.style.backgroundColor='transparent'; this.style.color='#D4AF37'; this.style.boxShadow='none';">
            <span class="flex items-center justify-center">
              <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
              </svg>
              Get Directions
            </span>
          </a>
        </div>
      </div>
    </section>

    <!-- Contact Form & Info -->
    <section class="py-24" style="background: linear-gradient(135deg, #0A0A0A 0%, #1A1A1A 50%, #0F0F0F 100%);">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid lg:grid-cols-2 gap-12">
          <!-- Contact Form -->
          <div class="relative overflow-hidden rounded-2xl shadow-2xl" style="background: linear-gradient(145deg, #1A1A1A 0%, #0F0F0F 100%); border: 2px solid rgba(212, 175, 55, 0.2);">
            <div class="absolute inset-0" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.05) 0%, transparent 50%, rgba(212, 175, 55, 0.05) 100%);"></div>
            <div class="relative p-8">
              <div class="mb-8">
                <div class="w-16 h-0.5 mb-4" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
                <h2 class="text-4xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Send us a Message</h2>
                <p class="text-sm" style="color: #D4AF37; font-family: 'Inter', sans-serif; font-weight: 500;">We'll get back to you within 24 hours</p>
              </div>
              
              <form @submit.prevent="submitForm" class="space-y-6">
                <div class="grid md:grid-cols-2 gap-4">
                  <div>
                    <label for="firstName" class="block text-sm font-medium mb-2" style="color: #F5F5F5; font-family: 'Inter', sans-serif;">First Name *</label>
                    <input 
                      type="text" 
                      id="firstName" 
                      v-model="form.firstName"
                      required
                      class="w-full px-4 py-3 rounded-lg focus:outline-none focus:ring-2 focus:border-transparent transition-all duration-300"
                      style="background-color: #0A0A0A; border: 1px solid rgba(212, 175, 55, 0.2); color: #F5F5F5; font-family: 'Inter', sans-serif;"
                      placeholder="Your first name"
                      onfocus="this.style.borderColor='#D4AF37'; this.style.boxShadow='0 0 0 3px rgba(212, 175, 55, 0.1)';"
                      onblur="this.style.borderColor='rgba(212, 175, 55, 0.2)'; this.style.boxShadow='none';"
                    >
                  </div>
                  <div>
                    <label for="lastName" class="block text-sm font-medium mb-2" style="color: #F5F5F5; font-family: 'Inter', sans-serif;">Last Name *</label>
                    <input 
                      type="text" 
                      id="lastName" 
                      v-model="form.lastName"
                      required
                      class="w-full px-4 py-3 rounded-lg focus:outline-none focus:ring-2 focus:border-transparent transition-all duration-300"
                      style="background-color: #0A0A0A; border: 1px solid rgba(212, 175, 55, 0.2); color: #F5F5F5; font-family: 'Inter', sans-serif;"
                      placeholder="Your last name"
                      onfocus="this.style.borderColor='#D4AF37'; this.style.boxShadow='0 0 0 3px rgba(212, 175, 55, 0.1)';"
                      onblur="this.style.borderColor='rgba(212, 175, 55, 0.2)'; this.style.boxShadow='none';"
                    >
                  </div>
                </div>

                <div>
                  <label for="email" class="block text-sm font-medium mb-2" style="color: #F5F5F5; font-family: 'Inter', sans-serif;">Email *</label>
                  <input 
                    type="email" 
                    id="email" 
                    v-model="form.email"
                    required
                    class="w-full px-4 py-3 rounded-lg focus:outline-none focus:ring-2 focus:border-transparent transition-all duration-300"
                    style="background-color: #0A0A0A; border: 1px solid rgba(212, 175, 55, 0.2); color: #F5F5F5; font-family: 'Inter', sans-serif;"
                    placeholder="your.email@example.com"
                    onfocus="this.style.borderColor='#D4AF37'; this.style.boxShadow='0 0 0 3px rgba(212, 175, 55, 0.1)';"
                    onblur="this.style.borderColor='rgba(212, 175, 55, 0.2)'; this.style.boxShadow='none';"
                  >
                </div>

                <div>
                  <label for="phone" class="block text-sm font-medium mb-2" style="color: #F5F5F5; font-family: 'Inter', sans-serif;">Phone</label>
                  <input 
                    type="tel" 
                    id="phone" 
                    v-model="form.phone"
                    class="w-full px-4 py-3 rounded-lg focus:outline-none focus:ring-2 focus:border-transparent transition-all duration-300"
                    style="background-color: #0A0A0A; border: 1px solid rgba(212, 175, 55, 0.2); color: #F5F5F5; font-family: 'Inter', sans-serif;"
                    placeholder="(555) 123-4567"
                    onfocus="this.style.borderColor='#D4AF37'; this.style.boxShadow='0 0 0 3px rgba(212, 175, 55, 0.1)';"
                    onblur="this.style.borderColor='rgba(212, 175, 55, 0.2)'; this.style.boxShadow='none';"
                  >
                </div>

                <div>
                  <label for="subject" class="block text-sm font-medium mb-2" style="color: #F5F5F5; font-family: 'Inter', sans-serif;">Subject *</label>
                  <select 
                    id="subject" 
                    v-model="form.subject"
                    required
                    class="w-full px-4 py-3 rounded-lg focus:outline-none focus:ring-2 focus:border-transparent transition-all duration-300"
                    style="background-color: #0A0A0A; border: 1px solid rgba(212, 175, 55, 0.2); color: #F5F5F5; font-family: 'Inter', sans-serif;"
                    onfocus="this.style.borderColor='#D4AF37'; this.style.boxShadow='0 0 0 3px rgba(212, 175, 55, 0.1)';"
                    onblur="this.style.borderColor='rgba(212, 175, 55, 0.2)'; this.style.boxShadow='none';"
                  >
                    <option value="">Select a subject</option>
                    <option value="general">General Inquiry</option>
                    <option value="liquor">Liquor Selection</option>
                    <option value="services">Services</option>
                    <option value="promotions">Promotions</option>
                    <option value="feedback">Feedback</option>
                    <option value="complaint">Complaint</option>
                    <option value="other">Other</option>
                  </select>
                </div>

                <div>
                  <label for="message" class="block text-sm font-medium mb-2" style="color: #F5F5F5; font-family: 'Inter', sans-serif;">Message *</label>
                  <textarea 
                    id="message" 
                    v-model="form.message"
                    required
                    rows="5" 
                    class="w-full px-4 py-3 rounded-lg focus:outline-none focus:ring-2 focus:border-transparent transition-all duration-300"
                    style="background-color: #0A0A0A; border: 1px solid rgba(212, 175, 55, 0.2); color: #F5F5F5; font-family: 'Inter', sans-serif;"
                    placeholder="Tell us how we can help you..."
                    onfocus="this.style.borderColor='#D4AF37'; this.style.boxShadow='0 0 0 3px rgba(212, 175, 55, 0.1)';"
                    onblur="this.style.borderColor='rgba(212, 175, 55, 0.2)'; this.style.boxShadow='none';"
                  ></textarea>
                </div>

                <button 
                  type="submit" 
                  :disabled="isSubmitting"
                  class="w-full py-4 px-6 rounded-lg font-semibold transition-all duration-300 transform hover:scale-105"
                  style="background-color: #D4AF37; color: #0A0A0A; font-family: 'Inter', sans-serif; font-weight: 600;"
                  onmouseover="this.style.backgroundColor='#E5C547'; this.style.boxShadow='0 8px 25px rgba(212, 175, 55, 0.3)';"
                  onmouseout="this.style.backgroundColor='#D4AF37'; this.style.boxShadow='none';"
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
              <div v-if="showSuccess" class="mt-6 p-6 rounded-lg" style="background-color: rgba(34, 197, 94, 0.1); border: 1px solid rgba(34, 197, 94, 0.3);">
                <div class="flex items-center">
                  <svg class="w-6 h-6 mr-3" style="color: #22C55E;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                  </svg>
                  <span class="font-medium" style="color: #22C55E; font-family: 'Inter', sans-serif;">Thank you! Your message has been sent successfully.</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Contact Information -->
          <div class="space-y-8">
            <!-- Store Info -->
            <div class="rounded-2xl p-8 shadow-2xl" style="background-color: #1A1A1A;">
              <div>
                <h3 class="text-2xl font-bold mb-6" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Store Information</h3>
                
                <div class="space-y-6">
                  <div class="flex items-start">
                    <div class="w-12 h-12 rounded-lg flex items-center justify-center mr-4" style="background-color: rgba(212, 175, 55, 0.1);">
                      <svg class="w-6 h-6" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
                      </svg>
                    </div>
                    <div>
                      <h4 class="font-semibold mb-1" style="color: #F5F5F5; font-family: 'Inter', sans-serif;">Address</h4>
                      <p class="mb-2" style="color: #F5F5F5; font-family: 'Inter', sans-serif;">3255 Viking Blvd NE<br>East Bethel, MN 55092</p>
                      <a href="https://maps.app.goo.gl/H1gsh7KUfgrg6ek49" target="_blank" class="transition-colors" style="color: #D4AF37; font-family: 'Inter', sans-serif;" onmouseover="this.style.color='#E5C547';" onmouseout="this.style.color='#D4AF37';">
                        Get Directions →
                      </a>
                    </div>
                  </div>

                  <div class="flex items-start">
                    <div class="w-12 h-12 rounded-lg flex items-center justify-center mr-4" style="background-color: rgba(212, 175, 55, 0.1);">
                      <svg class="w-6 h-6" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path>
                      </svg>
                    </div>
                    <div>
                      <h4 class="font-semibold mb-1" style="color: #F5F5F5; font-family: 'Inter', sans-serif;">Phone</h4>
                      <p class="mb-2" style="color: #F5F5F5; font-family: 'Inter', sans-serif;">(651) 395-2174</p>
                      <a href="tel:+16513952174" class="transition-colors" style="color: #D4AF37; font-family: 'Inter', sans-serif;" onmouseover="this.style.color='#E5C547';" onmouseout="this.style.color='#D4AF37';">
                        Call Now →
                      </a>
                    </div>
                  </div>

                  <div class="flex items-start">
                    <div class="w-12 h-12 rounded-lg flex items-center justify-center mr-4" style="background-color: rgba(212, 175, 55, 0.1);">
                      <svg class="w-6 h-6" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                      </svg>
                    </div>
                    <div>
                      <h4 class="font-semibold mb-1" style="color: #F5F5F5; font-family: 'Inter', sans-serif;">Email</h4>
                      <p class="mb-2" style="color: #F5F5F5; font-family: 'Inter', sans-serif;">info@goforitgas.com</p>
                      <a href="mailto:info@goforitgas.com" class="transition-colors" style="color: #D4AF37; font-family: 'Inter', sans-serif;" onmouseover="this.style.color='#E5C547';" onmouseout="this.style.color='#D4AF37';">
                        Send Email →
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Store Hours -->
            <div class="rounded-2xl p-8 shadow-2xl" style="background-color: #1A1A1A;">
              <div>
                <h3 class="text-2xl font-bold mb-6" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Store Hours</h3>
                
                <div class="space-y-3">
                  <div class="flex justify-between items-center">
                    <span class="font-medium" style="color: #F5F5F5; font-family: 'Inter', sans-serif;">Monday</span>
                    <span style="color: #D4AF37; font-family: 'Inter', sans-serif;">6:00 AM - 10:00 PM</span>
                  </div>
                  <div class="flex justify-between items-center">
                    <span class="font-medium" style="color: #F5F5F5; font-family: 'Inter', sans-serif;">Tuesday</span>
                    <span style="color: #D4AF37; font-family: 'Inter', sans-serif;">6:00 AM - 10:00 PM</span>
                  </div>
                  <div class="flex justify-between items-center">
                    <span class="font-medium" style="color: #F5F5F5; font-family: 'Inter', sans-serif;">Wednesday</span>
                    <span style="color: #D4AF37; font-family: 'Inter', sans-serif;">6:00 AM - 10:00 PM</span>
                  </div>
                  <div class="flex justify-between items-center">
                    <span class="font-medium" style="color: #F5F5F5; font-family: 'Inter', sans-serif;">Thursday</span>
                    <span style="color: #D4AF37; font-family: 'Inter', sans-serif;">6:00 AM - 10:00 PM</span>
                  </div>
                  <div class="flex justify-between items-center">
                    <span class="font-medium" style="color: #F5F5F5; font-family: 'Inter', sans-serif;">Friday</span>
                    <span style="color: #D4AF37; font-family: 'Inter', sans-serif;">6:00 AM - 10:00 PM</span>
                  </div>
                  <div class="flex justify-between items-center">
                    <span class="font-medium" style="color: #F5F5F5; font-family: 'Inter', sans-serif;">Saturday</span>
                    <span style="color: #D4AF37; font-family: 'Inter', sans-serif;">6:00 AM - 10:00 PM</span>
                  </div>
                  <div class="flex justify-between items-center">
                    <span class="font-medium" style="color: #F5F5F5; font-family: 'Inter', sans-serif;">Sunday</span>
                    <span style="color: #D4AF37; font-family: 'Inter', sans-serif;">6:00 AM - 10:00 PM</span>
                  </div>
                </div>
                
                <p class="text-sm mt-4" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">*Gas pumps available 24/7</p>
              </div>
            </div>

            <!-- Quick Actions -->
            <div class="rounded-2xl p-8 shadow-2xl" style="background-color: #1A1A1A;">
              <div>
                <h3 class="text-2xl font-bold mb-6" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Quick Actions</h3>
                
                <div class="space-y-4">
                  <a href="tel:+16513952174" class="w-full text-center block py-3 px-6 rounded-lg font-semibold transition-colors duration-300" style="background-color: #D4AF37; color: #0A0A0A; font-family: 'Inter', sans-serif;">
                    Call Now
                  </a>
                  <a href="https://maps.app.goo.gl/H1gsh7KUfgrg6ek49" target="_blank" class="w-full text-center block py-3 px-6 rounded-lg font-semibold transition-all duration-300 border-2" style="border-color: #D4AF37; color: #D4AF37; background: transparent; font-family: 'Inter', sans-serif;" onmouseover="this.style.backgroundColor='#D4AF37'; this.style.color='#0A0A0A';" onmouseout="this.style.backgroundColor='transparent'; this.style.color='#D4AF37';">
                    Get Directions
                  </a>
                  <NuxtLink to="/liquor" class="w-full text-center block py-3 px-6 rounded-lg font-semibold transition-colors duration-300" style="background-color: #D4AF37; color: #0A0A0A; font-family: 'Inter', sans-serif;">
                    View Liquor Collection
                  </NuxtLink>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Map Section -->
    <section class="py-16" style="background-color: #F5F5F5;">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="text-4xl font-bold mb-4" style="color: #0A0A0A; font-family: 'Playfair Display', serif;">Find Us</h2>
          <p class="text-xl" style="color: #0A0A0A; font-family: 'Inter', sans-serif;">Located conveniently in East Bethel, MN</p>
        </div>
        
        <div class="rounded-2xl shadow-2xl overflow-hidden" style="background-color: #F5F5F5; border: 2px solid #D4AF37;">
          <div class="p-0">
            <iframe 
              src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2805.4882811108355!2d-93.18742019999999!3d45.318761599999995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x52b31fd1ea2616b9%3A0xba7fee652ff8a42b!2sGo%20For%20It%20Liquor!5e0!3m2!1sen!2sca!4v1758400585801!5m2!1sen!2sca" 
              width="100%" 
              height="450" 
              style="border:0;" 
              allowfullscreen="" 
              loading="lazy" 
              referrerpolicy="no-referrer-when-downgrade"
              class="rounded-lg"
            ></iframe>
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
  title: 'Contact Us - Go For It Liquor',
  meta: [
    { name: 'description', content: 'Contact Go For It Liquor for questions, feedback, or inquiries. Located at 3255 Viking Blvd NE, East Bethel, MN 55092. Call (651) 395-2174 or visit us today.' },
    { name: 'keywords', content: 'contact, phone, address, directions, store hours, feedback, East Bethel, liquor store' }
  ]
})
</script>
