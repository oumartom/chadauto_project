
// ======================================================================================================================================================
// Gestion des formulaires (pour toutes les pages)
// ======================================================================================================================================================

function initForms() {
    // Gestion générique de tous les formulaires
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Ajout de l'identifiant du formulaire
            const formData = new FormData(this);
            formData.append('form_source', this.id);

            // Désactiver le bouton
            const submitBtn = this.querySelector('[type="submit"]');
            const originalText = submitBtn.textContent;
            submitBtn.disabled = true;
            submitBtn.textContent = 'Envoi en cours...';

            // Envoi AJAX
            fetch('send_email.php', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    alert('Message envoyé avec succès !');
                    this.reset();
                } else {
                    alert('Erreur: ' + data.message);
                }
            })
            .catch(error => {
                console.error('Erreur:', error);
                alert('Une erreur réseau est survenue');
            })
            .finally(() => {
                submitBtn.disabled = false;
                submitBtn.textContent = originalText;
            });
        });
    });
}

// Initialisation dans DOMContentLoaded
document.addEventListener('DOMContentLoaded', function() {
    initForms();
    // ... vos autres initialisations ...
});



// Gestion du formulaire de réservation pour la page d'accueil àààààààààààààààààààààààààààààààààààààààààààààààààà
// Gestion du formulaire de réservation pour la page d'accueil àààààààààààààààààààààààààààààààààààààààààààààààààà
 

// Gestion du formulaire de réservation
document.getElementById('reservationForm')?.addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Vérification du honeypot
    if (this.elements.company.value) {
        console.log('Spam attempt detected');
        return;
    }

    const formData = new FormData(this);
    const submitBtn = this.querySelector('button[type="submit"]');
    const originalText = submitBtn.textContent;

    // Désactiver le bouton pendant l'envoi
    submitBtn.disabled = true;
    submitBtn.textContent = 'Processing...';

    fetch('send_email.php', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const feedback = document.getElementById('form-feedback');
        feedback.textContent = data.message;
        feedback.className = `form-feedback ${data.status}`;
        
        if (data.status === 'success') {
            this.reset();
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('form-feedback').textContent = 
            'An error occurred. Please try again.';
    })
    .finally(() => {
        submitBtn.disabled = false;
        submitBtn.textContent = originalText;
    });
});

// Page langue ççççççççççççççççç ààààààààààààààààààààààààààààààààààààààààààààààààààtoutes les images de voiture
// Page langue ççççççççççççççççç ààààààààààààààààààààààààààààààààààààààààààààààààààtoutes les images de voiture
// Page langue ççççççççççççççççç ààààààààààààààààààààààààààààààààààààààààààààààààààtoutes les images de voiture
 


  
    // Page voiture ààààààààààààààààààààààààààààààààààààààààààààààààààtoutes les images de voiture
    // Page voiture ààààààààààààààààààààààààààààààààààààààààààààààààààtoutes les images de voiture
    // Page voiture ààààààààààààààààààààààààààààààààààààààààààààààààààtoutes les images de voiture


document.addEventListener("DOMContentLoaded", function() {
    // Sélectionner toutes les images de voiture
    const voitureImages = document.querySelectorAll('.voiture-image');

    // Ajouter un écouteur d'événements à chaque image
    voitureImages.forEach(image => {
        image.addEventListener('click', function() {
            // Basculer la classe 'zoomed' pour agrandir ou réduire l'image
            this.classList.toggle('zoomed');
        });
    });
});


// Page appartement ààààààààààààààààààààààààààààààààààààààààààààààààààtoutes les images de voiture
// Page appartement ààààààààààààààààààààààààààààààààààààààààààààààààààtoutes les images de voiture
// Page appartement ààààààààààààààààààààààààààààààààààààààààààààààààààtoutes les images de voiture

document.addEventListener("DOMContentLoaded", function() {
    // Sélectionner toutes les images d'appartement
    const appartementImages = document.querySelectorAll('.appartement-image');

    // Ajouter un écouteur d'événements à chaque image
    appartementImages.forEach(image => {
        image.addEventListener('click', function() {
            // Basculer la classe 'zoomed' pour agrandir ou réduire l'image
            this.classList.toggle('zoomed');
        });
    });
});



// Page réservation-voiture ààààààààààààààààààààààààààààààààààààààààààààààààààtoutes les images de voiture
// Page réservation-voiture ààààààààààààààààààààààààààààààààààààààààààààààààààtoutes les images de voiture
// Page réservation-voiture ààààààààààààààààààààààààààààààààààààààààààààààààààtoutes les images de voiture
 

// JavaScript spécifique à la page Réservation Voiture
document.addEventListener("DOMContentLoaded", function () {
    // Gestion du diaporama
    const diaporamaImages = document.querySelectorAll(".diaporama-image");
    let currentImageIndex = 0;

    function showNextImage() {
        diaporamaImages[currentImageIndex].classList.remove("active");
        currentImageIndex = (currentImageIndex + 1) % diaporamaImages.length;
        diaporamaImages[currentImageIndex].classList.add("active");
    }

    setInterval(showNextImage, 5000); // Change d'image toutes les 5 secondes

    // Gestion des boutons de réservation et des formulaires
    const reservationItems = document.querySelectorAll(".reservation-voiture-item");

    reservationItems.forEach((item) => {
        const reservationButton = item.querySelector(".reservation-button");
        const reservationForm = item.querySelector(".reservation-form");
        const reservationFormContent = item.querySelector(".reservation-form-content");

        // Afficher le formulaire au clic sur le bouton
        reservationButton.addEventListener("click", (event) => {
            event.stopPropagation(); // Empêcher la propagation du clic
            reservationForm.style.display = "block";
        });

        // Soumission du formulaire
        reservationFormContent.addEventListener("submit", (event) => {
            event.preventDefault(); // Empêcher le rechargement de la page

            // Récupérer les valeurs du formulaire
            const nom = reservationFormContent.querySelector("#nom").value;
            const email = reservationFormContent.querySelector("#email").value;
            const dateDebut = reservationFormContent.querySelector("#date-debut").value;
            const dateFin = reservationFormContent.querySelector("#date-fin").value;

            // Valider les champs (exemple simple)
            if (nom && email && dateDebut && dateFin) {
                // Afficher un message de confirmation
                alert(`Réservation confirmée pour ${nom} (${email}) du ${dateDebut} au ${dateFin}.`);
                // Réinitialiser le formulaire
                reservationFormContent.reset();
                // Masquer le formulaire
                reservationForm.style.display = "none";
            } else {
                alert("Veuillez remplir tous les champs du formulaire.");
            }
        });

        // Fermer le formulaire lorsqu'on clique en dehors
        window.addEventListener("click", (event) => {
            if (event.target !== reservationButton && !reservationForm.contains(event.target)) {
                reservationForm.style.display = "none";
            }
        });
    });
}); 



// Page réservation-appartement ààààààààààààààààààààààààààààààààààààààààààààààààààtoutes les images de voiture
// Page réservation-appartement ààààààààààààààààààààààààààààààààààààààààààààààààààtoutes les images de voiture
// Page réservation-appartement ààààààààààààààààààààààààààààààààààààààààààààààààààtoutes les images de voiture

  
// JavaScript spécifique à la page Réservation Appartement
document.addEventListener("DOMContentLoaded", function () {
    // Gestion du diaporama
    const diaporamaImages = document.querySelectorAll(".diaporama-image");
    let currentImageIndex = 0;

    function showNextImage() {
        diaporamaImages[currentImageIndex].classList.remove("active");
        currentImageIndex = (currentImageIndex + 1) % diaporamaImages.length;
        diaporamaImages[currentImageIndex].classList.add("active");
    }

    setInterval(showNextImage, 5000); // Change d'image toutes les 5 secondes

    // Gestion des boutons de réservation et des formulaires
    const reservationItems = document.querySelectorAll(".reservation-appartement-item");

    reservationItems.forEach((item) => {
        const reservationButton = item.querySelector(".reservation-button");
        const reservationForm = item.querySelector(".reservation-form");
        const reservationFormContent = item.querySelector(".reservation-form-content");

        // Afficher le formulaire au clic sur le bouton
        reservationButton.addEventListener("click", (event) => {
            event.stopPropagation(); // Empêcher la propagation du clic
            reservationForm.style.display = "block";
        });

        // Soumission du formulaire
        reservationFormContent.addEventListener("submit", (event) => {
            event.preventDefault(); // Empêcher le rechargement de la page

            // Récupérer les valeurs du formulaire
            const nom = reservationFormContent.querySelector("#nom").value;
            const email = reservationFormContent.querySelector("#email").value;
            const dateDebut = reservationFormContent.querySelector("#date-debut").value;
            const dateFin = reservationFormContent.querySelector("#date-fin").value;

            // Valider les champs (exemple simple)
            if (nom && email && dateDebut && dateFin) {
                // Afficher un message de confirmation
                alert(`Réservation confirmée pour ${nom} (${email}) du ${dateDebut} au ${dateFin}.`);
                // Réinitialiser le formulaire
                reservationFormContent.reset();
                // Masquer le formulaire
                reservationForm.style.display = "none";
            } else {
                alert("Veuillez remplir tous les champs du formulaire.");
            }
        });

        // Fermer le formulaire lorsqu'on clique en dehors
        window.addEventListener("click", (event) => {
            if (event.target !== reservationButton && !reservationForm.contains(event.target)) {
                reservationForm.style.display = "none";
            }
        });
    });
});

// Page réservation-les-deux ààààààààààààààààààààààààààààààààààààààààààààààààààtoutes les images de voiture
// Page réservation-les-deux ààààààààààààààààààààààààààààààààààààààààààààààààààtoutes les images de voiture
// Page réservation-les-deux ààààààààààààààààààààààààààààààààààààààààààààààààààtoutes les images de voiture

 
document.addEventListener("DOMContentLoaded", function() {
    // Gérer la soumission du formulaire combiné
    const reservationForm = document.querySelector('.reservation-form-content');
    reservationForm.addEventListener('submit', (e) => {
        e.preventDefault();

        // Récupérer les données du formulaire
        const nom = reservationForm.querySelector('#nom').value;
        const email = reservationForm.querySelector('#email').value;
        const telephone = reservationForm.querySelector('#telephone').value;
        const typeVoiture = reservationForm.querySelector('#type-voiture').value;
        const dateVoiture = reservationForm.querySelector('#date-voiture').value;
        const typeAppartement = reservationForm.querySelector('#type-appartement').value;
        const dateAppartement = reservationForm.querySelector('#date-appartement').value;

        // Valider les champs
        if (!typeVoiture || !typeAppartement) {
            alert('Veuillez sélectionner un type de voiture et un type d\'appartement.');
            return;
        }

        // Envoyer les données (simulation)
        console.log('Réservation combinée envoyée :', {
            nom,
            email,
            telephone,
            typeVoiture,
            dateVoiture,
            typeAppartement,
            dateAppartement
        });

        // Afficher un message d'alerte
        alert('Votre réservation combinée a été effectuée avec succès !');

        // Masquer le formulaire et réinitialiser les champs
        reservationForm.reset();
    });
});

    
// Page contact ààààààààààààààààààààààààààààààààààààààààààààààààààtoutes les images de voiture
// Page contact ààààààààààààààààààààààààààààààààààààààààààààààààààtoutes les images de voiture
// Page contact ààààààààààààààààààààààààààààààààààààààààààààààààààtoutes les images de voiture

// Diaporama
function initDiaporama() {
    const images = document.querySelectorAll('.diaporama img');

    if (images.length > 0) {
        let currentImageIndex = 0;

        function showNextImage() {
            images[currentImageIndex].classList.remove('active');
            currentImageIndex = (currentImageIndex + 1) % images.length;
            images[currentImageIndex].classList.add('active');
        }

        setInterval(showNextImage, 10000); // Change d'image toutes les 10 secondes
    }
}

// FAQ
function initFAQ() {
    document.querySelectorAll('.faq-question').forEach(question => {
        question.addEventListener('click', () => {
            const faqItem = question.parentElement;
            faqItem.classList.toggle('active');
            const toggleIcon = question.querySelector('.toggle-icon');
            toggleIcon.textContent = faqItem.classList.contains('active') ? '-' : '+';
        });
    });
}

// Validation du formulaire de contact
function initContactForm() {
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function (event) {
            event.preventDefault();
            alert('Votre message a été envoyé avec succès !');
            this.reset();
        });
    }
}

 
// Diaporama
function initDiaporama() {
    const images = document.querySelectorAll('.diaporama img');

    if (images.length > 0) {
        let currentImageIndex = 0;

        function showNextImage() {
            images[currentImageIndex].classList.remove('active');
            currentImageIndex = (currentImageIndex + 1) % images.length;
            images[currentImageIndex].classList.add('active');
        }

        setInterval(showNextImage, 10000); // Change d'image toutes les 10 secondes
    }
}

// FAQ
function initFAQ() {
    document.querySelectorAll('.faq-question').forEach(question => {
        question.addEventListener('click', () => {
            const faqItem = question.parentElement;
            faqItem.classList.toggle('active');
            const toggleIcon = question.querySelector('.toggle-icon');
            toggleIcon.textContent = faqItem.classList.contains('active') ? '-' : '+';
        });
    });
}

// Validation du formulaire de contact
function initContactForm() {
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function (event) {
            event.preventDefault();
            alert('Votre message a été envoyé avec succès !');
            this.reset();
        });
    }
}

// Gestion du changement de langue
function initLanguageSwitcher() {
    document.querySelectorAll('.dropdown-content a[data-lang]').forEach(langLink => {
        langLink.addEventListener('click', function (event) {
            event.preventDefault();
            const selectedLang = this.getAttribute('data-lang');
            alert(`Langue sélectionnée : ${selectedLang}`);
            // Ici, vous pouvez ajouter la logique pour changer la langue du site
        });
    });
}

// Initialisation des fonctionnalités
document.addEventListener('DOMContentLoaded', function () {
    initDiaporama();
    initFAQ();
    initContactForm();
    initLanguageSwitcher();
});


// Page langues ààààààààààààààààààààààààààààààààààààààààààààààààààtoutes les images de voiture
// Page langues ààààààààààààààààààààààààààààààààààààààààààààààààààtoutes les images de voiture
// Page langues ààààààààààààààààààààààààààààààààààààààààààààààààààtoutes les images de voiture


// Application du style à l'adaption de l'écran pour tout type d'appareil  ààààààààààààààààààààààààààààààààààààààààààààààààààtoutes les images de voiture
// Application du style à l'adaption de l'écran pour tout type d'appareil  ààààààààààààààààààààààààààààààààààààààààààààààààààtoutes les images de voiture
// Application du style à l'adaption de l'écran pour tout type d'appareil  ààààààààààààààààààààààààààààààààààààààààààààààààààtoutes les images de voiture
 

document.addEventListener('DOMContentLoaded', () => {
    // Gestion des menus déroulants
    document.querySelectorAll('.dropdown').forEach((dropdown) => {
      const link = dropdown.querySelector('a');
      const menu = dropdown.querySelector('.dropdown-menu');
  
      link.addEventListener('click', (e) => {
        e.preventDefault();
        menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
      });
  
      // Fermer le menu si on clique en dehors
      document.addEventListener('click', (e) => {
        if (!dropdown.contains(e.target)) {
          menu.style.display = 'none';
        }
      });
    });
  
    // ... (le reste de votre code JavaScript) ...
  });
  
  // ==================================================
  // Ajouts pour le Responsive Design
  // ==================================================
  
  // Gestion du diaporama pour les petits écrans
  const images = document.querySelectorAll('.diaporama img');
  let currentImageIndex = 0;
  
  function showNextImage() {
    images[currentImageIndex].classList.remove('active');
    currentImageIndex = (currentImageIndex + 1) % images.length;
    images[currentImageIndex].classList.add('active');
  }
  
  if (images.length > 0) {
    setInterval(showNextImage, 10000); // Change d'image toutes les 10 secondes
  }




  
// ...Envoi de mail et reception àààààààààà (votre code existant pour le diaporama, les menus déroulants, etc.) ...
// ...Envoi de mail et reception àààààààààà (votre code existant pour le diaporama, les menus déroulants, etc.) ...
// ...Envoi de mail et reception àààààààààà (votre code existant pour le diaporama, les menus déroulants, etc.) ...


// Gestion du formulaire de contact
document.getElementById('contactForm')?.addEventListener('submit', function (event) {
    event.preventDefault(); // Empêcher le rechargement de la page

    // Récupérer les données du formulaire
    const formData = new FormData(this);

    // Envoyer les données via AJAX
    fetch('php/send_email.php', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Afficher un message de confirmation ou d'erreur
        document.getElementById('responseMessage').textContent = data.message;
        if (data.status === 'success') {
            this.reset(); // Réinitialiser le formulaire
        }
    })
    .catch(error => {
        console.error('Erreur :', error);
        document.getElementById('responseMessage').textContent = "Une erreur s'est produite.";
    });
});

// Gestion du formulaire de réservation
document.getElementById('reservationForm')?.addEventListener('submit', function (event) {
    event.preventDefault(); // Empêcher le rechargement de la page

    // Récupérer les données du formulaire
    const formData = new FormData(this);

    // Envoyer les données via AJAX
    fetch('php/send_email.php', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Afficher un message de confirmation ou d'erreur
        document.getElementById('reservationResponse').textContent = data.message;
        if (data.status === 'success') {
            this.reset(); // Réinitialiser le formulaire
        }
    })
    .catch(error => {
        console.error('Erreur :', error);
        document.getElementById('reservationResponse').textContent = "Une erreur s'est produite.";
    });
});