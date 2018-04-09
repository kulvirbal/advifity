$(document).ready(function(){
    $('#autocomplete').autocomplete({
        source: '/search',
        onSelect: function (index) {
            var that = this,
                    onSelectCallback = that.options.onSelect,
                    suggestion = that.suggestions.length >= 1 ? that.suggestions[index] : that.suggestions;
        
            that.currentValue = that.getValue(suggestion.value);
        
            if (that.currentValue !== that.el.val() && !that.options.preserveInput) {
                that.el.val(that.currentValue);
            }
        
            that.signalHint(null);
            that.suggestions = [];
            that.selection = suggestion;
        
            if ($.isFunction(onSelectCallback)) {
                onSelectCallback.call(that.element, suggestion);
            }
        },
    })
    .data( "ui-autocomplete" )._renderItem = function( ul, item ) {
        console.log(item);
        return $( "<li></li>" ).data( "ui-autocomplete-item", item ).append('<a>'+item.value+'</a>' ).appendTo( ul );
    };
});
