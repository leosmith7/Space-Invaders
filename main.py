import turtle
from spaceship import Spaceship
from alien import Alien
from bullet import Bullet
import random
from scoreboard import Scoreboard
import time
from cover import Cover

screen = turtle.Screen()
screen.title("Space Invaders")
screen.bgcolor("black")
screen.tracer(0)
screen.setup(width=1200, height=800)

spaceship = Spaceship()

screen.listen()
screen.onkey(spaceship.move_left, "Left")
screen.onkey(spaceship.move_right, "Right")

bullets = []
alien_bullets = []
scoreboard = Scoreboard()

covers = [
    Cover((-300, -170)),
    Cover((0, -170)),
    Cover((300, -170))
]

level = 1
bullet_speed = 1
alien_speed = 15
alien_direction = 1  # 1 for right, -1 for left


def fire_bullet():
    if len(bullets) == 0:  # Only allow one bullet on screen at a time
        spaceship_position = spaceship.position()
        new_bullet = Bullet(spaceship_position, 1)  # Direction 1 (upward)
        bullets.append(new_bullet)


screen.onkey(fire_bullet, 'space')


def create_aliens():
    aliens.clear()
    for row in range(3):
        for col in range(8):
            x = -320 + col * 80
            y = 350 - row * 50
            alien = Alien((x, y))
            aliens.append(alien)


aliens = []
create_aliens()


def move_aliens():
    global alien_speed, alien_direction
    hit_wall = False

    # Check if any alien hits the wall
    for alien in aliens:
        x = alien.xcor()
        if x > 530 or x < -530:
            hit_wall = True
            break

    # If an alien hits the wall, reverse direction and move down
    if hit_wall:
        alien_direction *= -1
        for alien in aliens:
            alien.sety(alien.ycor() - 20)

    for alien in aliens:
        alien.setx(alien.xcor() + alien_speed * alien_direction)

    screen.ontimer(move_aliens, 500)


move_aliens()


def alien_shooting():
    if len(aliens) > 0:
        shooting_alien = random.choice(aliens)
        alien_position = shooting_alien.position()
        new_bullet = Bullet(alien_position, -1)  # Direction -1 (downward)
        alien_bullets.append(new_bullet)

    # Schedule the next alien shooting
    screen.ontimer(alien_shooting, random.randint(1000, 2000))


alien_shooting()

score_per_alien = 20
game_on = True
while game_on:
    screen.update()

    # Move spaceship bullets
    for bullet in bullets[:]:
        if not bullet.move(speed=bullet_speed):
            bullets.remove(bullet)
            bullet.hideturtle()
            del bullet
        else:
            # Check for collisions with aliens
            for alien in aliens[:]:
                if bullet.check_collision(alien):
                    bullets.remove(bullet)
                    bullet.hideturtle()
                    del bullet
                    alien.hideturtle()
                    aliens.remove(alien)
                    scoreboard.increase_score(score_per_alien)
                    break

                    # Move alien bullets
    for bullet in alien_bullets[:]:
        if not bullet.move(speed=bullet_speed):
            alien_bullets.remove(bullet)
            bullet.hideturtle()
            del bullet
        else:
            # Check for collisions with the player's spaceship
            if bullet.distance(spaceship) < 30:
                scoreboard.decrease_life()
                bullet.hideturtle()
                alien_bullets.remove(bullet)
                del bullet

                if scoreboard.lives == 0:
                    game_on = False
                    scoreboard.game_over()

                    # Check for collisions between aliens and the spaceship
    for alien in aliens[:]:
        if alien.distance(spaceship) < 30:
            game_on = False
            scoreboard.game_over()

            # Check for collisions between bullets and covers
    for bullet in bullets[:]:
        for cover in covers:
            if cover.isvisible() and bullet.distance(cover) < 50:
                cover.take_damage()
                bullets.remove(bullet)
                bullet.hideturtle()
                del bullet
                break

    for bullet in alien_bullets[:]:
        for cover in covers:
            if cover.isvisible() and bullet.distance(cover) < 50:
                cover.take_damage()
                alien_bullets.remove(bullet)
                bullet.hideturtle()
                del bullet
                break

                # Check if all aliens are destroyed
    if not aliens:
        scoreboard.increase_level()
        screen.update()
        time.sleep(2)

        # Clear all bullets from the screen
        for bullet in bullets[:]:
            bullet.hideturtle()
            bullets.remove(bullet)
        for bullet in alien_bullets[:]:
            bullet.hideturtle()
            alien_bullets.remove(bullet)

        create_aliens()
        alien_speed *= 1.1
        bullet_speed *= 2
        score_per_alien *= scoreboard.level
        move_aliens()

screen.exitonclick()
