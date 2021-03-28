 jQuery(function ($) {

        /* initialisation du bootstrap x-editable. Toutes les balises ayant class="modif" sont éditables*/
        $.fn.editable.defaults.mode = 'inline';
        $('.modif').editable({
            value: 'TBD',
            source: ['YES', 'NO', 'N/A','TBD']
        });
    });