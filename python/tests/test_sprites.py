from testgame.sprites import ActionImages

def test_actionimages():
    act = ActionImages()
    act.load_from_path('assassin')
    for action in act.action_images.keys():
        print(f'{action=} {len(action)=}')
    print(f'{len(act.action_images)=}')

# def test_assassin():
#     s = Assassin()
