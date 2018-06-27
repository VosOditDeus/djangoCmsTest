$(function () {

    let gridStack = $('.grid-stack');
    gridStack.gridstack();
    //TODO: REWORK THIS FOR GOD SAKE
    if (userType === 'normaluser') {
        gridStack.data('gridstack').disable();
        // $('.grid-stack').data('gridstack').movable('.grid-stack-item', false);
        // $('.grid-stack').data('gridstack').resizable('.grid-stack-item', false);
    }

    function saveGrid() {
        this.serializedData = _.map($('.grid-stack > .grid-stack-item:visible'), function (el) {
            el = $(el);
            var node = el.data('_gridstack_node');
            return {
                x: node.x,
                y: node.y,
                width: node.width,
                height: node.height,
                // content: $('.grid-stack-item-content', el).parent().html()
            };
        }, this);
        var items = GridStackUI.Utils.sort(this.serializedData);
        $.ajax({
            type: "GET",
            dataType: 'json',
            async: false,
            url: '/saveGrid',
            data: {
                items: items
            },
            success: () => {
                console.log('works!')
            },
            error: () => {
                console.log('error!')
            }
        })
        localStorage.setItem("items", JSON.stringify(items));
        console.log('grid is saved');
        return false;
    }

    // saveGrid();

    gridStack.on('change', function (event, items) {

        saveGrid();
    });
})