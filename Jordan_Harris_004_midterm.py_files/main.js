require.config({
	baseUrl: "",
	paths: {
		'core' : 'js/core',
		'libs' : 'js/libs',
		'underscore-clean': 'js/libs/underscore-module',
		'jquery': 'js/libs/jquery.min',
		'lsunderscore': 'js/libs/lsUnderscore',
		'backbone-noconflict': 'js/libs/backbone-module',
		'backbone-clean': 'js/libs/backbone-min',
		'backbone-with-validation' : 'js/libs/backboneWithValidation',
		'backbone': 'js/libs/lsbackbone',
		'handlebars-clean': 'js/libs/handlebars-module',
		'handlebars': 'js/libs/handlebars-withHelpers-module',
		'text': 'js/libs/text',
		'template': 'js/libs/template',
		'vuec' : 'js/libs/vue-loader',
		'vue' : 'js/libs/vue.runtime',
		'vuex' : 'js/libs/vuex',
		'vue-syncadapter' : 'js/libs/vue-syncadapter',
		'vue-componentcompiler': 'js/libs/vue-componentcompiler',
		'vue-util' : 'js/libs/vue-util',
		'postcss': 'js/libs/postcss'
	},
	packages: [{
		name: 'moment',
		location: 'app/plugins/moment',
		main: 'moment.min'
	}],
	map: {
		'*' : { 
				'backbone-clean' : 'backbone-noconflict',
				'underscore' : 'lsunderscore'
			},
		'backbone-noconflict' : { 'backbone-clean': 'backbone-clean' },
		'underscore' : {'lsunderscore' : 'lsunderscore'}
	}
});
