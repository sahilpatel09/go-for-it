<template>
  <div>
    <!-- Hero Section -->
    <section class="relative h-64 flex items-center justify-center overflow-hidden">
      <div class="absolute inset-0">
        <NuxtImg 
          src="/images/careers-hero.jpg" 
          alt="Join our team at Go For It Gas"
          class="w-full h-full object-cover"
        />
        <div class="hero-overlay"></div>
      </div>
      <div class="relative z-10 text-center text-white">
        <h1 class="heading-2 mb-4 text-shadow-lg">Join Our Team</h1>
        <p class="text-lg text-shadow">Be part of a growing, community-focused business</p>
      </div>
    </section>

    <!-- Why Work With Us -->
    <section class="py-16">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="heading-2 mb-4">Why Work at Go For It Gas?</h2>
          <p class="text-xl text-neutral-600">
            We're more than just a gas station – we're a community hub where people come together. 
            Join our team and be part of something meaningful.
          </p>
        </div>

        <div class="grid md:grid-cols-3 gap-8 mb-16">
          <div class="text-center">
            <div class="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"></path>
              </svg>
            </div>
            <h3 class="heading-4 mb-2">Great Team Environment</h3>
            <p class="text-neutral-600">Work with friendly, supportive colleagues who care about each other and our customers.</p>
          </div>

          <div class="text-center">
            <div class="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1"></path>
              </svg>
            </div>
            <h3 class="heading-4 mb-2">Competitive Benefits</h3>
            <p class="text-neutral-600">Health insurance, paid time off, employee discounts, and opportunities for advancement.</p>
          </div>

          <div class="text-center">
            <div class="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
              </svg>
            </div>
            <h3 class="heading-4 mb-2">Growth Opportunities</h3>
            <p class="text-neutral-600">Learn new skills, take on responsibilities, and advance your career with our growing business.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Open Positions -->
    <section class="py-16 bg-neutral-50">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="heading-2 mb-4">Open Positions</h2>
          <p class="text-xl text-neutral-600">Current job openings at Go For It Gas</p>
        </div>

        <div class="space-y-6">
          <!-- Cashier Position -->
          <div class="card">
            <div class="card-body">
              <div class="flex flex-col md:flex-row md:items-center md:justify-between mb-4">
                <div>
                  <h3 class="heading-3 mb-2">Cashier / Customer Service</h3>
                  <p class="text-neutral-600">Part-time & Full-time positions available</p>
                </div>
                <div class="mt-4 md:mt-0">
                  <span class="inline-block bg-accent-100 text-accent-800 text-sm font-medium px-3 py-1 rounded-full">Hiring Now</span>
                </div>
              </div>
              
              <div class="mb-4">
                <h4 class="font-semibold text-neutral-900 mb-2">Responsibilities:</h4>
                <ul class="text-neutral-600 space-y-1">
                  <li>• Operate cash register and process transactions</li>
                  <li>• Provide excellent customer service</li>
                  <li>• Stock shelves and maintain store cleanliness</li>
                  <li>• Handle fuel transactions and pump operations</li>
                </ul>
              </div>

              <div class="mb-4">
                <h4 class="font-semibold text-neutral-900 mb-2">Requirements:</h4>
                <ul class="text-neutral-600 space-y-1">
                  <li>• High school diploma or equivalent</li>
                  <li>• Previous retail/customer service experience preferred</li>
                  <li>• Ability to work flexible hours including weekends</li>
                  <li>• Friendly, outgoing personality</li>
                </ul>
              </div>

              <div class="flex flex-col sm:flex-row gap-3">
                <button @click="openApplication('cashier')" class="btn-primary">
                  Apply Now
                </button>
                <span class="text-sm text-neutral-500 self-center">Posted: December 1, 2024</span>
              </div>
            </div>
          </div>

          <!-- Service Technician Position -->
          <div class="card">
            <div class="card-body">
              <div class="flex flex-col md:flex-row md:items-center md:justify-between mb-4">
                <div>
                  <h3 class="heading-3 mb-2">Service Technician</h3>
                  <p class="text-neutral-600">Full-time position</p>
                </div>
                <div class="mt-4 md:mt-0">
                  <span class="inline-block bg-accent-100 text-accent-800 text-sm font-medium px-3 py-1 rounded-full">Hiring Now</span>
                </div>
              </div>
              
              <div class="mb-4">
                <h4 class="font-semibold text-neutral-900 mb-2">Responsibilities:</h4>
                <ul class="text-neutral-600 space-y-1">
                  <li>• Perform oil changes and basic automotive maintenance</li>
                  <li>• Operate and maintain car wash equipment</li>
                  <li>• Provide tire services and repairs</li>
                  <li>• Maintain service area cleanliness and safety</li>
                </ul>
              </div>

              <div class="mb-4">
                <h4 class="font-semibold text-neutral-900 mb-2">Requirements:</h4>
                <ul class="text-neutral-600 space-y-1">
                  <li>• Automotive experience preferred</li>
                  <li>• Ability to lift up to 50 pounds</li>
                  <li>• Valid driver's license</li>
                  <li>• Mechanical aptitude and attention to detail</li>
                </ul>
              </div>

              <div class="flex flex-col sm:flex-row gap-3">
                <button @click="openApplication('technician')" class="btn-primary">
                  Apply Now
                </button>
                <span class="text-sm text-neutral-500 self-center">Posted: November 28, 2024</span>
              </div>
            </div>
          </div>

          <!-- Assistant Manager Position -->
          <div class="card">
            <div class="card-body">
              <div class="flex flex-col md:flex-row md:items-center md:justify-between mb-4">
                <div>
                  <h3 class="heading-3 mb-2">Assistant Manager</h3>
                  <p class="text-neutral-600">Full-time position</p>
                </div>
                <div class="mt-4 md:mt-0">
                  <span class="inline-block bg-neutral-100 text-neutral-600 text-sm font-medium px-3 py-1 rounded-full">Coming Soon</span>
                </div>
              </div>
              
              <div class="mb-4">
                <h4 class="font-semibold text-neutral-900 mb-2">Responsibilities:</h4>
                <ul class="text-neutral-600 space-y-1">
                  <li>• Assist in daily store operations and staff management</li>
                  <li>• Handle customer complaints and resolve issues</li>
                  <li>• Manage inventory and ordering</li>
                  <li>• Train new employees</li>
                </ul>
              </div>

              <div class="mb-4">
                <h4 class="font-semibold text-neutral-900 mb-2">Requirements:</h4>
                <ul class="text-neutral-600 space-y-1">
                  <li>• 2+ years retail management experience</li>
                  <li>• Strong leadership and communication skills</li>
                  <li>• Availability for flexible scheduling</li>
                  <li>• Basic computer skills</li>
                </ul>
              </div>

              <div class="flex flex-col sm:flex-row gap-3">
                <button disabled class="btn-primary opacity-50 cursor-not-allowed">
                  Apply Soon
                </button>
                <span class="text-sm text-neutral-500 self-center">Expected: January 2025</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Application Form Modal -->
    <div v-if="showApplication" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div class="bg-white rounded-xl max-w-2xl w-full max-h-[90vh] overflow-y-auto">
        <div class="p-6">
          <div class="flex justify-between items-center mb-6">
            <h2 class="heading-2">Job Application</h2>
            <button @click="closeApplication" class="text-neutral-400 hover:text-neutral-600">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
              </svg>
            </button>
          </div>

          <form @submit.prevent="submitApplication" class="space-y-6">
            <div class="grid md:grid-cols-2 gap-4">
              <div>
                <label for="appFirstName" class="block text-sm font-medium text-neutral-700 mb-2">First Name *</label>
                <input 
                  type="text" 
                  id="appFirstName" 
                  v-model="application.firstName"
                  required
                  class="w-full px-3 py-2 border border-neutral-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                >
              </div>
              <div>
                <label for="appLastName" class="block text-sm font-medium text-neutral-700 mb-2">Last Name *</label>
                <input 
                  type="text" 
                  id="appLastName" 
                  v-model="application.lastName"
                  required
                  class="w-full px-3 py-2 border border-neutral-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                >
              </div>
            </div>

            <div class="grid md:grid-cols-2 gap-4">
              <div>
                <label for="appEmail" class="block text-sm font-medium text-neutral-700 mb-2">Email *</label>
                <input 
                  type="email" 
                  id="appEmail" 
                  v-model="application.email"
                  required
                  class="w-full px-3 py-2 border border-neutral-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                >
              </div>
              <div>
                <label for="appPhone" class="block text-sm font-medium text-neutral-700 mb-2">Phone *</label>
                <input 
                  type="tel" 
                  id="appPhone" 
                  v-model="application.phone"
                  required
                  class="w-full px-3 py-2 border border-neutral-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                >
              </div>
            </div>

            <div>
              <label for="appPosition" class="block text-sm font-medium text-neutral-700 mb-2">Position Applied For *</label>
              <input 
                type="text" 
                id="appPosition" 
                v-model="application.position"
                readonly
                class="w-full px-3 py-2 border border-neutral-300 rounded-lg bg-neutral-50"
              >
            </div>

            <div>
              <label for="appExperience" class="block text-sm font-medium text-neutral-700 mb-2">Relevant Experience</label>
              <textarea 
                id="appExperience" 
                v-model="application.experience"
                rows="4" 
                class="w-full px-3 py-2 border border-neutral-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                placeholder="Describe your relevant work experience..."
              ></textarea>
            </div>

            <div>
              <label for="appMessage" class="block text-sm font-medium text-neutral-700 mb-2">Why do you want to work at Go For It Gas?</label>
              <textarea 
                id="appMessage" 
                v-model="application.message"
                rows="3" 
                class="w-full px-3 py-2 border border-neutral-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                placeholder="Tell us why you're interested in joining our team..."
              ></textarea>
            </div>

            <div>
              <label for="appResume" class="block text-sm font-medium text-neutral-700 mb-2">Resume (Optional)</label>
              <input 
                type="file" 
                id="appResume" 
                accept=".pdf,.doc,.docx"
                class="w-full px-3 py-2 border border-neutral-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent"
              >
            </div>

            <div class="flex flex-col sm:flex-row gap-4">
              <button 
                type="submit" 
                :disabled="isSubmitting"
                class="btn-primary flex-1"
              >
                <span v-if="isSubmitting" class="loading-dots">
                  <div></div>
                  <div></div>
                  <div></div>
                </span>
                <span v-else>Submit Application</span>
              </button>
              <button 
                type="button" 
                @click="closeApplication"
                class="btn-outline flex-1"
              >
                Cancel
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const showApplication = ref(false)
const isSubmitting = ref(false)
const application = ref({
  firstName: '',
  lastName: '',
  email: '',
  phone: '',
  position: '',
  experience: '',
  message: ''
})

const openApplication = (position) => {
  application.value.position = position === 'cashier' ? 'Cashier / Customer Service' : 'Service Technician'
  showApplication.value = true
}

const closeApplication = () => {
  showApplication.value = false
  application.value = {
    firstName: '',
    lastName: '',
    email: '',
    phone: '',
    position: '',
    experience: '',
    message: ''
  }
}

const submitApplication = async () => {
  isSubmitting.value = true
  
  try {
    // Simulate form submission
    await new Promise(resolve => setTimeout(resolve, 2000))
    
    // Reset form and close modal
    closeApplication()
    
    // Show success message (you could add a toast notification here)
    alert('Thank you! Your application has been submitted successfully.')
    
  } catch (error) {
    console.error('Application submission error:', error)
    alert('There was an error submitting your application. Please try again.')
  } finally {
    isSubmitting.value = false
  }
}

useHead({
  title: 'Careers - Go For It Gas',
  meta: [
    { name: 'description', content: 'Join the Go For It Gas team! We\'re hiring cashiers, service technicians, and more. Great benefits, competitive pay, and a friendly work environment.' },
    { name: 'keywords', content: 'jobs, careers, employment, hiring, cashier, service technician, assistant manager, Your City' }
  ]
})
</script>
