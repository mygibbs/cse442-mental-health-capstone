"""empty message

Revision ID: 1fb4172f7c7d
Revises: 7b045daaf877
Create Date: 2019-04-21 21:50:15.597351

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fb4172f7c7d'
down_revision = '7b045daaf877'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('currstreak', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('lastlogin', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'lastlogin')
    op.drop_column('user', 'currstreak')
    # ### end Alembic commands ###
