# Set initial values for variables
transparent = True
is_cube = False
glass = False

# Empty list for colliders
colliders = []

# List of dictionaries representing bones and their properties
bones = [{'name':'body','pivot':[0.0, 0.8125, 0.125],'vertices':[[-0.3124999701976776, 0.3750000298023224, 0.5, -0.3124999701976776, 0.375, -0.5, 0.3124999701976776, 0.375, -0.5, 0.3124999701976776, 0.3750000298023224, 0.5],
                                                                 [0.3124999701976776, 0.8750000596046448, 0.5, 0.3124999701976776, 0.875, -0.5, -0.3124999701976776, 0.875, -0.5, -0.3124999701976776, 0.8750000596046448, 0.5],
                                                                 [-0.3124999701976776, 0.375, -0.5, -0.3124999701976776, 0.875, -0.5, 0.3124999701976776, 0.875, -0.5, 0.3124999701976776, 0.375, -0.5], [0.3124999701976776, 0.3750000298023224, 0.5, 0.3124999701976776, 0.8750000596046448, 0.5, -0.3124999701976776, 0.8750000596046448, 0.5, -0.3124999701976776, 0.3750000298023224, 0.5],
                                                                 [0.3124999701976776, 0.3750000298023224, 0.5, 0.3124999701976776, 0.375, -0.5, 0.3124999701976776, 0.875, -0.5, 0.3124999701976776, 0.8750000596046448, 0.5],
                                                                 [-0.3124999701976776, 0.8750000596046448, 0.5, -0.3124999701976776, 0.875, -0.5, -0.3124999701976776, 0.375, -0.5, -0.3124999701976776, 0.3750000298023224, 0.5]],
          'tex_coords':[[0.056338028169014086, 0.0, 0.056338028169014086, 0.6666666666666667, 0.1267605633802817, 0.6666666666666667, 0.1267605633802817, 0.0], [0.18309859154929578, 0.0, 0.18309859154929578, 0.6666666666666667, 0.2535211267605634, 0.6666666666666667, 0.2535211267605634, 0.0],
                        [0.056338028169014086, 0.6666666666666667, 0.056338028169014086, 1.0, 0.1267605633802817, 1.0, 0.1267605633802817, 0.6666666666666667], [0.1267605633802817, 0.6666666666666667, 0.1267605633802817, 1.0, 0.19718309859154928, 1.0, 0.19718309859154928, 0.6666666666666667],
                        [0.1267605633802817, 0.0, 0.1267605633802817, 0.6666666666666667, 0.18309859154929578, 0.6666666666666667, 0.18309859154929578, 0.0], [0.0, 0.0, 0.0, 0.6666666666666667, 0.056338028169014086, 0.6666666666666667, 0.056338028169014086, 0.0]],
          'shading_values':[[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]}, {'name':'head','pivot':[0.0, 0.75, -0.375],'vertices':[[-0.25, 0.5, -0.875, -0.25, 1.0, -0.875, 0.25, 1.0, -0.875, 0.25, 0.5, -0.875], [0.25, 0.5, -0.375, 0.25, 1.0, -0.375, -0.25, 1.0, -0.375, -0.25, 0.5, -0.375], [-0.25, 1.0, -0.875, -0.25, 1.0, -0.375, 0.25, 1.0, -0.375, 0.25, 1.0, -0.875],
                                                                                                                                                                                                                         [0.25, 0.5, -0.875, 0.25, 0.5, -0.375, -0.25, 0.5, -0.375, -0.25, 0.5, -0.875], [0.25, 0.5, -0.875, 0.25, 1.0, -0.875, 0.25, 1.0, -0.375, 0.25, 0.5, -0.375], [-0.25, 0.5, -0.375, -0.25, 1.0, -0.375, -0.25, 1.0, -0.875, -0.25, 0.5, -0.875], 
                                                                                                                                                                                                                         [-0.125, 0.5625, -0.9375, -0.125, 0.75, -0.9375, 0.125, 0.75, -0.9375, 0.125, 0.5625, -0.9375], [0.125, 0.5625, -0.875, 0.125, 0.75, -0.875, -0.125, 0.75, -0.875, -0.125, 0.5625, -0.875], [-0.125, 0.75, -0.9375, -0.125, 0.75, -0.875, 0.125, 0.75, -0.875, 0.125, 0.75, -0.9375], 
                                                                                                                                                                                                                         [0.125, 0.5625, -0.9375, 0.125, 0.5625, -0.875, -0.125, 0.5625, -0.875, -0.125, 0.5625, -0.9375], [0.125, 0.5625, -0.9375, 0.125, 0.75, -0.9375, 0.125, 0.75, -0.875, 0.125, 0.5625, -0.875], [-0.125, 0.5625, -0.875, -0.125, 0.75, -0.875, -0.125, 0.75, -0.9375, -0.125, 0.5625, -0.9375]],
                                                                                                                                                                   'tex_coords':[[0.30985915492957744, 0.33333333333333337, 0.30985915492957744, 0.6666666666666667, 0.36619718309859156, 0.6666666666666667, 0.36619718309859156, 0.33333333333333337], [0.4225352112676056, 0.33333333333333337, 0.4225352112676056, 0.6666666666666667, 0.4788732394366197, 0.6666666666666667, 0.4788732394366197, 0.33333333333333337],
                                                                                                                                                                                 [0.30985915492957744, 0.6666666666666667, 0.30985915492957744, 1.0, 0.36619718309859156, 1.0, 0.36619718309859156, 0.6666666666666667], [0.36619718309859156, 0.6666666666666667, 0.36619718309859156, 1.0, 0.4225352112676056, 1.0, 0.4225352112676056, 0.6666666666666667], 
                                                                                                                                                                                 [0.36619718309859156, 0.33333333333333337, 0.36619718309859156, 0.6666666666666667, 0.4225352112676056, 0.6666666666666667, 0.4225352112676056, 0.33333333333333337], [0.2535211267605634, 0.33333333333333337, 0.2535211267605634, 0.6666666666666667, 0.30985915492957744, 0.6666666666666667, 0.30985915492957744, 0.33333333333333337], 
                                                                                                                                                                                 [0.4859154929577465, 0.8333333333333334, 0.4859154929577465, 0.9583333333333334, 0.5140845070422535, 0.9583333333333334, 0.5140845070422535, 0.8333333333333334], [0.5211267605633803, 0.8333333333333334, 0.5211267605633803, 0.9583333333333334, 0.5492957746478874, 0.9583333333333334, 0.5492957746478874, 0.8333333333333334], 
                                                                                                                                                                                 [0.4859154929577465, 0.9583333333333334, 0.4859154929577465, 1.0, 0.5140845070422535, 1.0, 0.5140845070422535, 0.9583333333333334], [0.5140845070422535, 0.9583333333333334, 0.5140845070422535, 1.0, 0.5422535211267606, 1.0, 0.5422535211267606, 0.9583333333333334], [0.5140845070422535, 0.8333333333333334, 0.5140845070422535, 0.9583333333333334, 0.5211267605633803, 0.9583333333333334, 0.5211267605633803, 0.8333333333333334], [0.4788732394366197, 0.8333333333333334, 0.4788732394366197, 0.9583333333333334, 0.4859154929577465, 0.9583333333333334, 0.4859154929577465, 0.8333333333333334]],'shading_values':[[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]}, {'name':'leg0','pivot':[-0.1875, 0.375, 0.4375],'vertices':[[-0.3125, 0.0, 0.3125, -0.3125, 0.375, 0.3125, -0.0625, 0.375, 0.3125, -0.0625, 0.0, 0.3125], [-0.0625, 0.0, 0.5625, -0.0625, 0.375, 0.5625, -0.3125, 0.375, 0.5625, -0.3125, 0.0, 0.5625], [-0.3125, 0.375, 0.3125, -0.3125, 0.375, 0.5625, -0.0625, 0.375, 0.5625, -0.0625, 0.375, 0.3125], [-0.0625, 0.0, 0.3125, -0.0625, 0.0, 0.5625, -0.3125, 0.0, 0.5625, -0.3125, 0.0, 0.3125], [-0.0625, 0.0, 0.3125, -0.0625, 0.375, 0.3125, -0.0625, 0.375, 0.5625, -0.0625, 0.0, 0.5625], [-0.3125, 0.0, 0.5625, -0.3125, 0.375, 0.5625, -0.3125, 0.375, 0.3125, -0.3125, 0.0, 0.3125]],'tex_coords':[[0.5774647887323944, 0.5833333333333333, 0.5774647887323944, 0.8333333333333334, 0.6056338028169014, 0.8333333333333334, 0.6056338028169014, 0.5833333333333333], [0.6338028169014085, 0.5833333333333333, 0.6338028169014085, 0.8333333333333334, 0.6619718309859155, 0.8333333333333334, 0.6619718309859155, 0.5833333333333333], [0.5774647887323944, 0.8333333333333334, 0.5774647887323944, 1.0, 0.6056338028169014, 1.0, 0.6056338028169014, 0.8333333333333334], [0.6056338028169014, 0.8333333333333334, 0.6056338028169014, 1.0, 0.6338028169014085, 1.0, 0.6338028169014085, 0.8333333333333334], [0.6056338028169014, 0.5833333333333333, 0.6056338028169014, 0.8333333333333334, 0.6338028169014085, 0.8333333333333334, 0.6338028169014085, 0.5833333333333333], [0.5492957746478874, 0.5833333333333333, 0.5492957746478874, 0.8333333333333334, 0.5774647887323944, 0.8333333333333334, 0.5774647887323944, 0.5833333333333333]],'shading_values':[[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]}, {'name':'leg1','pivot':[0.1875, 0.375, 0.4375],'vertices':[[0.0625, 0.0, 0.3125, 0.0625, 0.375, 0.3125, 0.3125, 0.375, 0.3125, 0.3125, 0.0, 0.3125], [0.3125, 0.0, 0.5625, 0.3125, 0.375, 0.5625, 0.0625, 0.375, 0.5625, 0.0625, 0.0, 0.5625], [0.0625, 0.375, 0.3125, 0.0625, 0.375, 0.5625, 0.3125, 0.375, 0.5625, 0.3125, 0.375, 0.3125], [0.3125, 0.0, 0.3125, 0.3125, 0.0, 0.5625, 0.0625, 0.0, 0.5625, 0.0625, 0.0, 0.3125], [0.3125, 0.0, 0.3125, 0.3125, 0.375, 0.3125, 0.3125, 0.375, 0.5625, 0.3125, 0.0, 0.5625], [0.0625, 0.0, 0.5625, 0.0625, 0.375, 0.5625, 0.0625, 0.375, 0.3125, 0.0625, 0.0, 0.3125]],'tex_coords':[[0.6901408450704225, 0.5833333333333333, 0.6901408450704225, 0.8333333333333334, 0.7183098591549296, 0.8333333333333334, 0.7183098591549296, 0.5833333333333333], [0.7464788732394366, 0.5833333333333333, 0.7464788732394366, 0.8333333333333334, 0.7746478873239436, 0.8333333333333334, 0.7746478873239436, 0.5833333333333333], [0.6901408450704225, 0.8333333333333334, 0.6901408450704225, 1.0, 0.7183098591549296, 1.0, 0.7183098591549296, 0.8333333333333334], [0.7183098591549296, 0.8333333333333334, 0.7183098591549296, 1.0, 0.7464788732394366, 1.0, 0.7464788732394366, 0.8333333333333334], [0.7183098591549296, 0.5833333333333333, 0.7183098591549296, 0.8333333333333334, 0.7464788732394366, 0.8333333333333334, 0.7464788732394366, 0.5833333333333333], [0.6619718309859155, 0.5833333333333333, 0.6619718309859155, 0.8333333333333334, 0.6901408450704225, 0.8333333333333334, 0.6901408450704225, 0.5833333333333333]],'shading_values':[[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]}, {'name':'leg2','pivot':[-0.1875, 0.375, -0.3125],'vertices':[[-0.3125, 0.0, -0.4375, -0.3125, 0.375, -0.4375, -0.0625, 0.375, -0.4375, -0.0625, 0.0, -0.4375], [-0.0625, 0.0, -0.1875, -0.0625, 0.375, -0.1875, -0.3125, 0.375, -0.1875, -0.3125, 0.0, -0.1875], [-0.3125, 0.375, -0.4375, -0.3125, 0.375, -0.1875, -0.0625, 0.375, -0.1875, -0.0625, 0.375, -0.4375], [-0.0625, 0.0, -0.4375, -0.0625, 0.0, -0.1875, -0.3125, 0.0, -0.1875, -0.3125, 0.0, -0.4375], [-0.0625, 0.0, -0.4375, -0.0625, 0.375, -0.4375, -0.0625, 0.375, -0.1875, -0.0625, 0.0, -0.1875], [-0.3125, 0.0, -0.1875, -0.3125, 0.375, -0.1875, -0.3125, 0.375, -0.4375, -0.3125, 0.0, -0.4375]],'tex_coords':[[0.8028169014084507, 0.5833333333333333, 0.8028169014084507, 0.8333333333333334, 0.8309859154929577, 0.8333333333333334, 0.8309859154929577, 0.5833333333333333], [0.8591549295774648, 0.5833333333333333, 0.8591549295774648, 0.8333333333333334, 0.8873239436619719, 0.8333333333333334, 0.8873239436619719, 0.5833333333333333], [0.8028169014084507, 0.8333333333333334, 0.8028169014084507, 1.0, 0.8309859154929577, 1.0, 0.8309859154929577, 0.8333333333333334], [0.8309859154929577, 0.8333333333333334, 0.8309859154929577, 1.0, 0.8591549295774648, 1.0, 0.8591549295774648, 0.8333333333333334], [0.8309859154929577, 0.5833333333333333, 0.8309859154929577, 0.8333333333333334, 0.8591549295774648, 0.8333333333333334, 0.8591549295774648, 0.5833333333333333], [0.7746478873239436, 0.5833333333333333, 0.7746478873239436, 0.8333333333333334, 0.8028169014084507, 0.8333333333333334, 0.8028169014084507, 0.5833333333333333]],'shading_values':[[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]}, {'name':'leg3','pivot':[0.1875, 0.375, -0.3125],'vertices':[[0.0625, 0.0, -0.4375, 0.0625, 0.375, -0.4375, 0.3125, 0.375, -0.4375, 0.3125, 0.0, -0.4375], [0.3125, 0.0, -0.1875, 0.3125, 0.375, -0.1875, 0.0625, 0.375, -0.1875, 0.0625, 0.0, -0.1875], [0.0625, 0.375, -0.4375, 0.0625, 0.375, -0.1875, 0.3125, 0.375, -0.1875, 0.3125, 0.375, -0.4375], [0.3125, 0.0, -0.4375, 0.3125, 0.0, -0.1875, 0.0625, 0.0, -0.1875, 0.0625, 0.0, -0.4375], [0.3125, 0.0, -0.4375, 0.3125, 0.375, -0.4375, 0.3125, 0.375, -0.1875, 0.3125, 0.0, -0.1875], [0.0625, 0.0, -0.1875, 0.0625, 0.375, -0.1875, 0.0625, 0.375, -0.4375, 0.0625, 0.0, -0.4375]],'tex_coords':[[0.9154929577464789, 0.5833333333333333, 0.9154929577464789, 0.8333333333333334, 0.9436619718309859, 0.8333333333333334, 0.9436619718309859, 0.5833333333333333], [0.971830985915493, 0.5833333333333333, 0.971830985915493, 0.8333333333333334, 1.0, 0.8333333333333334, 1.0, 0.5833333333333333], [0.9154929577464789, 0.8333333333333334, 0.9154929577464789, 1.0, 0.9436619718309859, 1.0, 0.9436619718309859, 0.8333333333333334], [0.9436619718309859, 0.8333333333333334, 0.9436619718309859, 1.0, 0.971830985915493, 1.0, 0.971830985915493, 0.8333333333333334], [0.9436619718309859, 0.5833333333333333, 0.9436619718309859, 0.8333333333333334, 0.971830985915493, 0.8333333333333334, 0.971830985915493, 0.5833333333333333], [0.8873239436619719, 0.5833333333333333, 0.8873239436619719, 0.8333333333333334, 0.9154929577464789, 0.8333333333333334, 0.9154929577464789, 0.5833333333333333]],'shading_values':[[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]}]
